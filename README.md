# CompTeleBot
Telegram bot designed to compile code from different languages and return the output and stats about the compilation process.

![Alt text](https://image.ibb.co/kCC7G8/telegram_bot.png "Logo")
***
## **Prerequisites**

This bot was built using [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI "pyTelegramBotAPI").

To install this API, simply run: (must have pip installed)

```
$ pip install pyTelegramBotAPI
```

Finally, you will need an API telegram bot token. You can obtain one using the [@BotFather](https://core.telegram.org/bots#botfather "BotFather").

***
## **Run**

If you already have installed the API and obtained a bot API, simply clone the repository, update your bot token in 'compbot.py' and run:

```python
python3 compbot.py
```

To test the bot, try sending:

```python
/comp python3 print("Hello World!")
```

If everything went right, you should recieve the following message:


```
Output: 
Hello World!

Stats: Absolute running time: 0.13 sec, cpu time: 0.09 sec, memory peak: 6 Mb, absolute service time: 0,14 sec
```
