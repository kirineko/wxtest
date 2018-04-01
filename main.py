# -*- coding: utf-8 -*-
# filename: main.py
import web
import bots
from handle import Handle

urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    bots.bots
    app = web.application(urls, globals())
    app.run()
