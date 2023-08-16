# -*- coding: utf-8 -*-
"""
wsgi module.
"""

from menu import MenuApplication


app = MenuApplication()


if __name__ == '__main__':
    app.run()
