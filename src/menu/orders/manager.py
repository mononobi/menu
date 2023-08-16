# -*- coding: utf-8 -*-
"""
orders manager module.
"""

import pyrin.validator.services as validator_services
import pyrin.filtering.services as filtering_services

from pyrin.core.globals import _
from pyrin.core.structs import Manager
from pyrin.database.services import get_current_store

from menu.orders import OrdersPackage


class OrdersManager(Manager):
    """
    orders manager class.
    """

    package_class = OrdersPackage
