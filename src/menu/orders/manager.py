# -*- coding: utf-8 -*-
"""
orders manager module.
"""

import pyrin.configuration.services as config_services
import pyrin.validator.services as validator_services

from pyrin.core.structs import Manager

import menu.telegram.services as telegram_services

from menu.orders import OrdersPackage
from menu.orders.exceptions import OrderNotFoundError, OrderStateCannotBeChangedError
from menu.orders.models import OrderEntity


class OrdersManager(Manager):
    """
    orders manager class.
    """

    package_class = OrdersPackage

    def _get_notification_message(self, title, order_id):
        """
        gets the notification message for the given order.

        :param str title: title to be used in the message.
        :param int order_id: order id to fill the notification message from its values.

        :rtype: str
        """

        entity = self.get(order_id)
        on_list_message = 'View order on list:'
        if entity.state == OrderEntity.StateEnum.OPEN:
            on_list_message = 'Change order state:'

        open_count = self.get_count(OrderEntity.StateEnum.OPEN)
        total_count = self.get_count()
        client_url = config_services.get_active('orders', 'client_url')
        message = (f'{title}\n\n'
                   f'Name: {entity.name}\n'
                   f'Item: {OrderEntity.ItemEnum(entity.item)}\n'
                   f'Count: {entity.count}\n'
                   f'State: {OrderEntity.StateEnum(entity.state)}\n'
                   f'Comment: {entity.comment or "-"}\n\n'
                   f'Open orders: {open_count}\n'
                   f'Total orders: {total_count}\n\n'
                   f'{on_list_message}\n{client_url}/orders?id={entity.id}\n\n'
                   f'View order:\n{client_url}/orders/{entity.id}\n\n'
                   f'View open orders:\n{client_url}/orders?state=OPEN\n\n'
                   f'View all orders:\n{client_url}/orders')

        return message

    def get_welcome_message(self, **options):
        """
        gets a welcome message.
        """

        return 'Welcome to the Birthday Party!'

    def notify_order_created(self, order_id):
        """
        notifies that an order has been created.

        :param int order_id: created order id.
        """

        mono_chat_id = config_services.get_active('telegram', 'mono_chat_id')
        mohi_chat_id = config_services.get_active('telegram', 'mohi_chat_id')
        message = self._get_notification_message('A NEW ORDER HAS BEEN ADDED.', order_id)

        telegram_services.send_message(mohi_chat_id, message)
        telegram_services.send_message(mono_chat_id, message)

    def notify_order_updated(self, order_id):
        """
        notifies that an order has been updated.

        :param int order_id: updated order id.
        """

        mono_chat_id = config_services.get_active('telegram', 'mono_chat_id')
        mohi_chat_id = config_services.get_active('telegram', 'mohi_chat_id')
        message = self._get_notification_message(f'ORDER [{order_id}] HAS BEEN EDITED.',
                                                 order_id)

        telegram_services.send_message(mohi_chat_id, message)
        telegram_services.send_message(mono_chat_id, message)

    def get_count(self, state=None):
        """
        gets the order count in the given state.

        :param str state: order state.
                          if set to None, total order count would be returned.
        :enum state:
            OPEN = 'OPEN'
            DONE = 'DONE'
            CANCELED = 'CANCELED'

        :rtype: int
        """

        query = OrderEntity.query(OrderEntity.id)
        if state is not None:
            query = query.where(OrderEntity.state == state)

        return query.count()

    def get(self, order_id):
        """
        gets the order with the given id.

        :param int order_id: order id to get.

        :rtype: OrderEntity
        """

        entity = OrderEntity.query().get(order_id)
        if not entity:
            raise OrderNotFoundError(f'Order [{order_id}] not found.')

        return entity

    def _change_state(self, order_id, state):
        """
        changes the state of the given order.

        :param int order_id: order id to change its state.
        :param str state: new state to be set for the order.
        :enum state:
            OPEN = 'OPEN'
            DONE = 'DONE'
            CANCELED = 'CANCELED'
        """

        entity = self.get(order_id)
        if entity.state != OrderEntity.StateEnum.OPEN:
            raise OrderStateCannotBeChangedError(f'Order [{order_id}] is in '
                                                 f'[{OrderEntity.StateEnum(entity.state)}] '
                                                 f'state and its state cannot be modified.')

        validator_services.validate(OrderEntity, lazy=False, state=state)
        entity.state = state
        entity.save()

        mono_chat_id = config_services.get_active('telegram', 'mono_chat_id')
        mohi_chat_id = config_services.get_active('telegram', 'mohi_chat_id')
        message = self._get_notification_message(f'ORDER [{order_id}] STATE '
                                                 f'HAS BEEN CHANGED TO [{state}].',
                                                 order_id)

        telegram_services.send_message(mohi_chat_id, message)
        telegram_services.send_message(mono_chat_id, message)

    def mark_done(self, order_id):
        """
        marks the given order as done.

        :param int order_id: order id to be marked as done.
        """

        self._change_state(order_id, OrderEntity.StateEnum.DONE)

    def mark_canceled(self, order_id):
        """
        marks the given order as canceled.

        :param int order_id: order id to be marked as canceled.
        """

        self._change_state(order_id, OrderEntity.StateEnum.CANCELED)
