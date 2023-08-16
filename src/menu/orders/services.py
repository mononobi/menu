# -*- coding: utf-8 -*-
"""
orders services module.
"""

from pyrin.application.services import get_component

from menu.orders import OrdersPackage


def get_welcome_message(**options):
    """
    gets a welcome message.
    """

    return get_component(OrdersPackage.COMPONENT_NAME).get_welcome_message(**options)
