# -*- coding: utf-8 -*-
"""
orders api module.
"""

from pyrin.api.router.decorators import api, post, put, patch, delete

import menu.orders.services as orders_services


# Usage:
# you could implement different api functions here and call corresponding service method this way:
# return orders_services.method_name(*arg, **kwargs)
