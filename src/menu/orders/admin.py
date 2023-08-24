# -*- coding: utf-8 -*-
"""
orders admin module.
"""

from pyrin.admin.decorators import admin
from pyrin.admin.page.base import AdminPage
from pyrin.admin.page.decorators import action
from pyrin.core.enumerations import HTTPMethodEnum

import menu.orders.services as order_services

from menu.orders.models import OrderEntity


@admin()
class OrderAdmin(AdminPage):
    entity = OrderEntity
    register_name = 'orders'
    name = 'Order'
    category = 'ORDERS'
    list_ordering = ('-created_at', '-id')
    list_fields = (OrderEntity.id, OrderEntity.name, OrderEntity.count,
                   OrderEntity.state, OrderEntity.item, OrderEntity.created_at,
                   OrderEntity.comment, 'mark_done', 'mark_canceled')
    remove_permission = False
    remove_all_permission = False

    @classmethod
    def _create(cls, **data):
        """
        creates an entity with given data.

        it's preferred for this method to return the pk of created entity
        if it is not a composite primary key. this lets the client fill
        fk fields automatically after create.

        :keyword **data: all data to be passed to create method.

        :rtype: int
        """

        order_id = super()._create(**data)
        order_services.notify_order_created(order_id)

    @classmethod
    def _update(cls, pk, **data):
        """
        updates an entity with given data.

        :param int pk: entity primary key to be updated.

        :keyword **data: all data to be passed to update method.

        :raises EntityNotFoundError: entity not found error.
        """

        super()._update(pk, **data)
        order_services.notify_order_updated(pk)

    @action
    def mark_done(self, row):
        """
        marks the current order as done.

        :param ROW_RESULT row: row entity.

        :rtype: dict
        """

        if row.state == OrderEntity.StateEnum.OPEN:
            return self._get_action_info('Mark Done',
                                         'menu.orders.api.mark_done',
                                         HTTPMethodEnum.PATCH,
                                         success_message=
                                         f'Order [{row.id}] marked as ['
                                         f'{OrderEntity.StateEnum(OrderEntity.StateEnum.DONE)}'
                                         f'] successfully.',
                                         url_params=dict(order_id=row.id))

        return None

    @action
    def mark_canceled(self, row):
        """
        marks the current order as canceled.

        :param ROW_RESULT row: row entity.

        :rtype: dict
        """

        if row.state == OrderEntity.StateEnum.OPEN:
            return self._get_action_info('Mark Canceled',
                                         'menu.orders.api.mark_canceled',
                                         HTTPMethodEnum.PATCH,
                                         success_message=
                                         f'Order [{row.id}] marked as ['
                                         f'{OrderEntity.StateEnum(OrderEntity.StateEnum.CANCELED)}'
                                         f'] successfully.',
                                         url_params=dict(order_id=row.id))

        return None
