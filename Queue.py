class Queue():
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, value):
        self.queue.append(value)
 
    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            print("Queue is emplty")
            return None
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(self.queue)



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()
