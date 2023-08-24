# -*- coding: utf-8 -*-
"""
orders api module.
"""

from pyrin.api.router.decorators import api, patch

import menu.orders.services as orders_services


@api('/birthday-party/welcome', authenticated=False)
def get_welcome_message(**options):
    """
    gets a welcome message.
    """

    return orders_services.get_welcome_message(**options)


@patch('/birthday-party/orders/<int:order_id>/done', authenticated=False)
def mark_done(order_id, **options):
    """
    marks the given order as done.

    :param int order_id: order id to be marked as done.
    """

    return orders_services.mark_done(order_id)


@patch('/birthday-party/orders/<int:order_id>/cancel', authenticated=False)
def mark_canceled(order_id, **options):
    """
    marks the given order as canceled.

    :param int order_id: order id to be marked as canceled.
    """

    return orders_services.mark_canceled(order_id)
