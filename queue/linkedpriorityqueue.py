# !/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/2/22 9:28
# @Author  : Despicable Me
# @Email   : 
# @File    : linkedpriorityqueue.py
# @Software: PyCharm
# @Explain :

from node import Node
from linkedqueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):

    def __init__(self, sourceCollection = None):
        LinkedQueue.__init__(self, sourceCollection)

    def add(self, item):

        if self.isEmpty() or self._rear.data <= item:
            LinkedQueue.add(item)
        else:
            probe = self._front
            while probe.data <= item:
                trailer = probe
                probe = probe.next
            newnode = Node(item, probe)
            if probe == self._front:
                self._front = newnode
            else:
                trailer.next = newnode
            self._size += 1