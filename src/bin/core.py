from sys import exit
from os import system
from platform import architecture


class Core(object):
    def __init__(self):
        pass

    @staticmethod
    def end(self):
        exit()

    @staticmethod
    def get_bit():
        return architecture()[0]

    @staticmethod
    def get_os_type(self):
        return architecture()[1]

    @staticmethod
    def wipe_console(self):
        if architecture()[1] == 'WindowsPE':
            system('cls')
        else:
            system('clear')
