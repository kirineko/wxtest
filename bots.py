from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance

@singleton
class Bots:
    deepThought = ChatBot("deepThought")
    deepThought.set_trainer(ChatterBotCorpusTrainer)
    # 使用中文语料库训练它
    deepThought.train("chatterbot.corpus.chinese")  # 语料库
    # Of course you can have any attributes or methods you like.

#bots = Bots()
