# -*- coding: utf-8 -*-
"""
orders admin module.
"""

from pyrin.admin.decorators import admin
from pyrin.admin.page.base import AdminPage

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
                   OrderEntity.comment)
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
