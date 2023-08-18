# -*- coding: utf-8 -*-
"""
telegram package.
"""

from pyrin.packaging.base import Package


class TelegramPackage(Package):
    """
    telegram package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'telegram.component'
    CONFIG_STORE_NAMES = ['telegram']
