# -*- coding: utf-8 -*-
# filename: code.py
import web
import aiboot
from handle import Handle

urls = (
    '/wx', 'Handle',
)



app = web.application(urls, globals())
application = app.wsgifunc()
app.run()