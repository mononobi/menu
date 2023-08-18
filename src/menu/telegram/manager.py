# -*- coding: utf-8 -*-
"""
telegram manager module.
"""

import requests

import pyrin.configuration.services as config_services
import pyrin.logging.services as logging_services

from pyrin.core.structs import Manager

from menu.telegram import TelegramPackage


class TelegramManager(Manager):
    """
    telegram manager class.
    """

    package_class = TelegramPackage

    def __init__(self):
        """
        initializes an instance of `TelegramManager`.
        """

        super().__init__()

        temp = config_services.get_active("telegram", "remote_url")
        self._remote_url = temp.format(token=config_services.get_active("telegram",
                                                                        "api_token"))

    def send_message(self, chat_id, message):
        """
        sends a message to the given chat.

        :param int chat_id: chat id to send message to.
        :param str message: message to be sent.
        """

        try:
            result = requests.post(self._remote_url,
                                   json=dict(chat_id=chat_id, text=message))

            result.raise_for_status()

        except Exception as error:
            logging_services.error(str(error))
