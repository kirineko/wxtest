# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


urls = (
    '/wx', 'Handle',
)

deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
deepThought.train("chatterbot.corpus.chinese")  # 语料库

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()