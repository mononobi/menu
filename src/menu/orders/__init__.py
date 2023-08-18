# -*- coding: utf-8 -*-
"""
orders package.
"""

from pyrin.packaging.base import Package


class OrdersPackage(Package):
    """
    orders package class.
    """

    NAME = __name__
    COMPONENT_NAME = 'orders.component'
    CONFIG_STORE_NAMES = ['orders']
