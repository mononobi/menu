# -*- coding: utf-8 -*-
"""
permission manager module.
"""

from pyrin.security.permission.manager import PermissionManager as BasePermissionManager
from pyrin.core.exceptions import CoreNotImplementedError

from menu.security.permission import PermissionPackage


class PermissionManager(BasePermissionManager):
    """
    permission manager class.
    """

    package_class = PermissionPackage

    def _exists(self, *primary_key):
        """
        gets a value indicating that given permission exists in database.

        the input parameters could be as many as needed arguments to
        represent the primary key of your permission entity.
        if you don't want to use permissions concept in your application,
        you could leave this method unimplemented.

        :param object primary_key: permission primary key value.

        :rtype: bool
        """

        raise CoreNotImplementedError()
