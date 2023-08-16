# -*- coding: utf-8 -*-
"""
orders exceptions module.
"""

from pyrin.core.exceptions import CoreException, CoreBusinessException


class OrdersException(CoreException):
    """
    orders exception.
    """
    pass


class OrdersBusinessException(CoreBusinessException, OrdersException):
    """
    orders business exception.
    """
    pass
