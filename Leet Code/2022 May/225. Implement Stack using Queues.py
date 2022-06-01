class MyStack:
    
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        if len(self.queue) == 0: 
            return True
        else:
            return False