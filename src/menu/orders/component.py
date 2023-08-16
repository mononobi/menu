# -*- coding: utf-8 -*-
"""
orders component module.
"""

from pyrin.application.decorators import component
from pyrin.application.structs import Component

from menu.orders import OrdersPackage
from menu.orders.manager import OrdersManager


@component(OrdersPackage.COMPONENT_NAME)
class OrdersComponent(Component, OrdersManager):
    """
    orders component class.
    """
    pass
