# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
    '/wx', 'Handle',
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
