"""
raven.transport.aiohttp
~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2014 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
# Skip flake8, python2 version doesn't recognize `yield from` statement
# flake8: noqa
from __future__ import absolute_import

from raven.exceptions import APIError, RateLimited
from raven.transport.base import AsyncTransport
from raven.transport.http import HTTPTransport

import socket

try:
    import aiohttp
    import asyncio
    has_aiohttp = True
except:
    has_aiohttp = False


class AioHttpTransport(AsyncTransport, HTTPTransport):
    pass
