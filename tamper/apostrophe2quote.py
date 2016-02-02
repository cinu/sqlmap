#!/usr/bin/env python

"""
Copyright (c) 2006-2015 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.LOWEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Replaces apostrophe chararacter with quotation mark

    >>> tamper("1 AND '1'='1")
    '1 AND "1"="1'
    """

    return payload.replace('\'', '\"') if payload else payload
