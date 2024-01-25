#
from datetime import date
import re


class Line():
    def print_line(self):
        print('=' * 30)


class ListClass(Line):
    def __init__(self):
        self.some_list = ['a', 'b', 'c']

    def get_data(self):
        print(self.some_list)
        self.print_line()


class DictClass(Line):
    def __init__(self):
        self.some_dict = {
            'EWR': 'Newark',
            'SFO': 'San Francisco',
            'RDU': 'Raleigh-Durham',
            'SJC': 'San Jose',
            'ABQ': 'Albuquerque',
            'OAK': 'Oakland',
            'SAC': 'Sacramento',
            'IAD': 'Dulles',
        }

    def get_data(self):
        for key, value in self.some_dict.items():
            print(key, value)
        self.print_line()


class Wombat():
    def __init__(self, i):
        self.id = i
        self.rx = re.compile("wombat")
        self.listclass = ListClass()
        self.dictclass = DictClass()
        self.date = date(2016, 5, i)


class Yeti():
    def __init__(self, i):
        self.id = i
        self.rx = re.compile("yeti")
        self.listclass = ListClass()
        self.dictclass = DictClass()
        self.date = date(2016, 6, i)
