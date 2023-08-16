# -*- coding: utf-8 -*-
"""
orders api module.
"""

from pyrin.api.router.decorators import api, post, put, patch, delete

import menu.orders.services as orders_services


@api('/birthday-party/welcome', authenticated=False)
def get_welcome_message(**options):
    """
    gets a welcome message.
    """

    return orders_services.get_welcome_message(**options)
