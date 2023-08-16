# -*- coding: utf-8 -*-
"""
security package.
"""

from pyrin.security import SecurityPackage as BaseSecurityPackage


class SecurityPackage(BaseSecurityPackage):
    """
    security package class.
    """

    NAME = __name__

    # if you want to extend pyrin's security manager in your application,
    # you should remove the below `COMPONENT_NAME` attribute to get
    # its value from the parent class to be able to extend the parent
    # package implementation.
    COMPONENT_NAME = None
