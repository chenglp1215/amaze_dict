#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 16:17
# @Author  : chenglongping
# @File    : amaze_dict.py
from __future__ import unicode_literals

import logging

logger = logging.getLogger(__name__)


class LeafBase(object):
    def __new__(cls, value=None):
        if value is None:
            type_class = type("LB_None", (object,), {
                "__getattr__": lambda x, key: x,
                "find_child": lambda x, key: x,
                "is_none": property(lambda x: True),
                "__bool__": lambda x: False,
                "__eq__": lambda x, v: True if v is value else False
            })
            return type_class()

        elif isinstance(value, bool):
            type_class = type("LB_%s" % (bool(value)), (object,), {
                "__getattr__": lambda x: LeafBase(),
                "find_child": lambda x: LeafBase(),
                "is_none": property(lambda x: False),
                "__bool__": lambda x: value,
                "__eq__": lambda x, v: True if v is value else False
            })
            return type_class()
        else:
            type_class = type("LB_%s" % (type(value)), (type(value),), {
                "__getattr__": lambda x, key: LeafBase(x.get(key)) if isinstance(x, dict) else LeafBase(),
                "find_child": lambda x, key: getattr(x, key),
                "is_none": property(lambda x: False),
                "__bool__": lambda x: bool(value)
            })
            return type_class(value)


def wrap_value(value):
    return LeafBase(value)
