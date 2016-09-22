class BusinessTasks(object):
    def getTask(self, list, n):
        linked_list = LinkedListCircular()
        for task in list:
            linked_list.insert_tail(Node(task))
        current = linked_list.head
        while linked_list.length > 1:
            for _ in xrange(n % linked_list.length):
                current = current.next
            linked_list.delete(current.prev)
        return current.key


class LinkedListCircular(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, x):
        x.next = self.head
        if self.head is not None:
            tail = self.head.prev
            self.head.prev = x
            x.prev = tail
            tail.next = x
        else:
            x.next = x
            x.prev = x
        self.head = x
        self.length += 1

    def insert_tail(self, x):
        self.insert(x)
        self.head = x.next

    def delete(self, x):
        if self.head.next is self.head:
            self.head = None
        else:
            x.next.prev = x.prev
            x.prev.next = x.next
        self.length -= 1

    def search(self, k):
        x = self.head
        for _ in xrange(self.length):
            if x.key == k:
                return x
            x = x.next
        return None


class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

if __name__ == '__main__':
    print BusinessTasks().getTask(["a", "b", "c", "d"], 2)
