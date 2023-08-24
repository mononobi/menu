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


def notify_order_created(order_id):
    """
    notifies that an order has been created.

    :param int order_id: created order id.
    """

    return get_component(OrdersPackage.COMPONENT_NAME).notify_order_created(order_id)


def notify_order_updated(order_id):
    """
    notifies that an order has been updated.

    :param int order_id: updated order id.
    """

    return get_component(OrdersPackage.COMPONENT_NAME).notify_order_updated(order_id)


def mark_done(order_id):
    """
    marks the given order as done.

    :param int order_id: order id to be marked as done.
    """

    return get_component(OrdersPackage.COMPONENT_NAME).mark_done(order_id)


def mark_canceled(order_id):
    """
    marks the given order as canceled.

    :param int order_id: order id to be marked as canceled.
    """

    return get_component(OrdersPackage.COMPONENT_NAME).mark_canceled(order_id)
