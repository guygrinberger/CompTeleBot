import sys
sys.path.append('..')
from Rextester import Rextester, RextesterException #Rextester util file
import csv #for opening 'languages.csv'
import telebot #pyTelegramBotAPI
import logging #for debug log

token = '' #insert telebot token here (keep '')

bot = telebot.TeleBot(token) #create bot
logger = telebot.logger #initialize logger
telebot.logger.setLevel(logging.DEBUG) #print debug on console
rextester = Rextester()

#'/start' or '/help' 
@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    start_string = """I'm a compiler bot! I compile code
    here are my avalidable commands:
    1. /comp <language> <code> (to compile code)
    2. /lang (to see a list of supported languages)"""

    bot.reply_to(message, start_string)

#'/lang' command to display supported languages
@bot.message_handler(commands=['lang'])
def handle_languages(message):
    input_file = csv.DictReader(open("languages.csv"))
    response = "This are the supported languages:\n"
    for row in input_file:
        response += row["id"] + ". " + row["name"].lower()
        response += "\n"

    bot.reply_to(message,response)

#returns 1 if the provided language is supported. otherwise, returns -1
def is_supported(language):
    input_file = csv.DictReader(open("languages.csv"))
    for row in input_file:
        if row["name"].lower() == language.lower():
            return 1
    
    return -1

#'/comp' command is the compile command.
#language name and code need to be passed as arguments.
@bot.message_handler(commands=['comp'])
def handle_comp(message):
    message_text = message.text

    #at least 3 arguments
    if len(message_text.split()) < 3:
        bot.reply_to(message, "Not enough arguments (< 3)")
        return

    #add '/stdin' to message before code
    stdin = ''
    if "/stdin" in message_text:
        stdin = ' '.join(message_text.split('/stdin ')[1:])
        message_text = message_text.replace('/stdin ' + stdin, '')

    language = message_text.split()[1]
    code = ' '.join(message_text.split()[2:])

    #check if provided language is supported
    if is_supported(language) == -1:
        bot.reply_to(message, "Language is not supported")
        return

    try:
        response = rextester.execute(language=language, code=code, stdin=stdin)
    except RextesterException: 
        bot.send_message(message.chat.id, 'error @ rextester (site error)')
        return

    #if compilation resulted in warnings and/or errors
    extra = ''
    if response['Warnings']:
        extra = extra + '\nWarning: ' + response['Warnings']
    if response['Errors']:
        extra = extra + '\nErrors: ' + response['Errors']

    #collect stats about compilation
    stats = ''
    if response['Stats']:
        stats = '\nStats: ' + response['Stats']

    output = ' no output '
    if response['Result']:
        output = response['Result']

    if len(extra) < 4070:  # prevent "too long message" errors
        bot.send_message(message.chat.id, 'Output: \n' + output[:(4080 - len(extra) - len(stats))] + extra + stats)
    else:
        bot.send_message(message.chat.id, 'too much long errors/warnings to show output')

#unkown command handler
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_unkown(message):
    bot.send_message(message.chat.id, "Sorry, I don't understand \"" + message.text 
    + "\"\nSee all avalidable commands at /help")

if __name__ == "__main__":
    bot.polling()
    bot.idle() #to be able to send ^C signal

while True:
    try:
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        exit(0)
    except Exception as e:
        continue
