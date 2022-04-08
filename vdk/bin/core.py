from datetime import datetime


class Core(object):
    def __init__(self):
        pass

    @staticmethod
    def log(self, msg: str):
        print(f'[{datetime.now().time()}]: {msg}')

    def end(self):
        self.log('Application ended.')
