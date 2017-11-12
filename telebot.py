# coding: utf-8
"""Telegram Bot API integration."""
import requests
import json
import sys


class Bot:
    """The bot class."""

    def __init__(self, access_token):
        """Set up the access_token and defines the request URL.

        Args:
            @param (str): Telegram access token.
        """
        self.access_token = access_token
        self.url = "https://api.telegram.org/bot" + access_token + "/"

    def get_me(self):
        """Return information about the bot.

        Returns:
            Dict with the bot information.

        """
        method = self.url + 'getme'
        return json.loads(requests.post(method).content)

    def send_message(self, chat_id, text):
        """Send a message to the chat.

        Args:
            @param chat_id (int): The chat_id (which is also the user id)
            @param text (str): Message
        Returns:
            Dict with the request response.

        """
        method = self.url + 'sendMessage'
        params = {"chat_id": chat_id, "text": text}
        return json.loads(requests.post(method, data=params).content)

    def get_updates(self, update_id=0):
        """Get messages updates.

        If update_id is set, return messages after the update+Id.

        Args:
            @param update_id (int): Telegram update_id

        Returns:
            Dict with the messages.

        """
        method = self.url + 'getUpdates'
        params = update_id and ("?offset=" + update_id) or ""
        return json.loads(requests.get(method + params).content)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print('Usage: python telebot.py YOUR_ACCESS_TOKEN')
        sys.exit(1)
    token = sys.argv[1]
    bot = Bot(token)
    print(bot.get_me())
