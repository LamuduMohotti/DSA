Class Queues():
    def _init_(self):
        self.queue = []

    # Add an element
    def enqueue(self, value):
        self.queue.append(value)
 
    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            print("Queue is emplty")
            return None
        return self.queue[-1]

    # Display the queue
