# -*- coding: utf-8 -*-
"""
orders models module.
"""

from sqlalchemy import Unicode, Integer

from pyrin.core.enumerations import CoreEnum, EnumMember
from pyrin.database.model.declarative import CoreEntity
from pyrin.database.model.mixin import CreateHistoryMixin
from pyrin.database.orm.sql.schema.base import CoreColumn
from pyrin.database.orm.sql.schema.columns import AutoPKColumn, GUIDPKColumn, \
    SequencePKColumn, FKColumn, IntegerColumn, SmallIntegerColumn, DateColumn, \
    TimeStampColumn, DateTimeColumn, BooleanColumn, HiddenColumn, StringColumn, \
    TextColumn, BigIntegerColumn


class OrderEntity(CoreEntity, CreateHistoryMixin):

    _table = 'order'

    class ItemEnum(CoreEnum):
        SPECIAL_COCKTAIL = EnumMember('SPECIAL_COCKTAIL', 'Special Cocktail')

    class CountEnum(CoreEnum):
        ONE = EnumMember(1, '1')
        TWO = EnumMember(2, '2')
        THREE = EnumMember(3, '3')
        FOUR = EnumMember(4, '4')

    class StateEnum(CoreEnum):
        OPEN = EnumMember('OPEN', 'Open')
        DONE = EnumMember('DONE', 'Done')
        CANCELED = EnumMember('CANCELED', 'Canceled')

    id = AutoPKColumn(name='id')
    name = StringColumn(name='name', nullable=False, max_length=64)
    item = StringColumn(name='item', nullable=False, max_length=64,
                        check_in=ItemEnum, default=ItemEnum.SPECIAL_COCKTAIL)
    count = IntegerColumn(name='count', nullable=False,
                          check_in=CountEnum, default=CountEnum.ONE)
    state = StringColumn(name='state', nullable=False, max_length=64,
                         check_in=StateEnum, default=StateEnum.OPEN)
    comment = StringColumn(name='comment', max_length=100)
