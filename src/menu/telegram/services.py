# -*- coding: utf-8 -*-
"""
telegram services module.
"""

from pyrin.application.services import get_component

from menu.telegram import TelegramPackage


def send_message(chat_id, message):
    """
    sends a message to the given chat.

    :param int chat_id: chat id to send message to.
    :param str message: message to be sent.
    """

    return get_component(TelegramPackage.COMPONENT_NAME).send_message(chat_id, message)
