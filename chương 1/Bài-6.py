class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def print_stack(self):
        for item in reversed(self.stack):  # In ngược từ cuối đến đầu
            print(item)
def main():
    stack = Stack()
    stack.push("thuoc")
    stack.pop()
    stack.is_empty()
    stack.size()
    stack.print_stack()
if __name__ == '__main__':
    main()