#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import threading


class ChatThread(threading.Thread):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)