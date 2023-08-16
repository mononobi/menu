# -*- coding: utf-8 -*-
"""
orders admin module.
"""

from pyrin.admin.decorators import admin
from pyrin.admin.page.base import AdminPage

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
    # list_indexed = True
    # list_page_size = 2
