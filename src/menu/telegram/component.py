# -*- coding: utf-8 -*-
"""
telegram component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from menu.telegram import TelegramPackage
from menu.telegram.manager import TelegramManager


@component(TelegramPackage.COMPONENT_NAME)
class TelegramComponent(Component, TelegramManager):
    """
    telegram component class.
    """
    pass
