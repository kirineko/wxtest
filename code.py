# -*- coding: utf-8 -*-
# filename: code.py
import web
import aiboot
from handle import Handle

urls = (
    '/wx', 'Handle',
)

app = web.application(urls, globals())
wsgiapp = app.wsgifunc()
