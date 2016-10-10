class SmartWordToy(object):
    def minPresses(self, start, finish, forbid):
        forbidden = [False] * (26 ** 4)
        presses = [None] * (26 ** 4)
        presses[self.get_code(start)] = 0
        for f in forbid:
            groups = f.split()
            for c1 in groups[0]:
                for c2 in groups[1]:
                    for c3 in groups[2]:
                        for c4 in groups[3]:
                            code = self.get_code(c1 + c2 + c3 + c4)
                            forbidden[code] = True
        Q = Queue()
        Q.enqueue(start)
        while not Q.empty():
            u = Q.dequeue()
            current = presses[self.get_code(u)]
            if u == finish:
                return current
            for v in self.get_neighbours(u):
                code = self.get_code(v)
                if not forbidden[code] and presses[code] is None:
                    presses[code] = current + 1
                    Q.enqueue(v)
        # ans = presses[self.get_code(finish)]
        # return ans if ans is not None else -1
        return -1

    def get_code(self, s):
        code = 0
        for i, c in enumerate(s):
            code += (ord(c) - ord("a")) * 26**i
        return code

    def minPresses2(self, start, finish, forbid):
        forbid = [s.split() for s in forbid]
        visited = set()
        visited.add(start)
        boundary = [start]
        presses = -1
        while boundary:
            next_boundary = []
            presses += 1
            for u in boundary:
                if u == finish:
                    return presses
                for v in self.get_neighbours(u):
                    if v not in visited:
                        visited.add(v)
                        if not self.forbidden(v, forbid):
                            next_boundary.append(v)
            boundary = next_boundary
        return -1

    def get_neighbours(self, v):
        for i, c in enumerate(v):
            yield v[:i] + chr((ord(c) - ord("a") - 1) % 26 + ord("a")) + v[i+1:]
            yield v[:i] + chr((ord(c) - ord("a") + 1) % 26 + ord("a")) + v[i+1:]

    def forbidden(self, v, forbid):
        return any(all(c in group[i] for i, c in enumerate(v)) for group in forbid)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def insert(self, x):
        x.next = self.head
        if not self.empty():
            self.head.prev = x
        else:
            self.tail = x
        self.head = x
        x.prev = None

    def insert_tail(self, x):
        x.prev = self.tail
        if not self.empty():
            self.tail.next = x
        else:
            self.head = x
        self.tail = x
        x.next = None

    def delete(self, x):
        if x.next is not None:
            x.next.prev = x.prev
        else:
            self.tail = x.prev
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x


class Queue(LinkedList):
    def enqueue(self, x):
        self.insert_tail(Node(x))

    def dequeue(self):
        if self.empty():
            return None
        node = self.head
        self.delete(self.head)
        return node.key

    def peek(self):
        if self.empty():
            return None
        return self.head.key


class Node(object):
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


if __name__ == '__main__':
    # print SmartWordToy().minPresses("aaaa", "zzzz", ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"])
    print SmartWordToy().minPresses("aaaa", "bbbb", ["b b b b"])
    # print SmartWordToy().minPresses("aaaa", "mmnn", [])
