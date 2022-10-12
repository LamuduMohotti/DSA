# Stack data structure in python

class Stack():
    def __init__(self, value):
        self.stack = []

    # Adding an element
    def push(self, value):
        self.stack.append(value)
