# telebot
Simple Telegram Bot

### Example usage:

#### Information about the bot
```python
from telebot import Bot

token = "YOUR_TELEGRAM_ACCESS_TOKEN"
bot = Bot(token)
print(bot.get_me())
```

#### Get messages updates
```python
from telebot import Bot

token = "YOUR_TELEGRAM_ACCESS_TOKEN"
bot = Bot(token)
print(bot.get_updates())
```

#### Send message to a chat (or user)
```python
from telebot import Bot

token = "YOUR_TELEGRAM_ACCESS_TOKEN"
bot = Bot(token)
chat_id = 123456789
message = "I come in peace"
print(bot.send_message(chat_id, message))
```
