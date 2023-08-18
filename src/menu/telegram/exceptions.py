# -*- coding: utf-8 -*-
"""
telegram exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class TelegramException(CoreException):
    """
    telegram exception.
    """
    pass


class TelegramBusinessException(CoreBusinessException, TelegramException):
    """
    telegram business exception.
    """
    pass
