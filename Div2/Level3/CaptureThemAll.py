class CaptureThemAll(object):
    def fastKnight(self, knight, rook, queen):
        # Convert cr strings to row, col coordinates.
        knight = self.transform_to_coordinates(knight)
        rook = self.transform_to_coordinates(rook)
        queen = self.transform_to_coordinates(queen)
        # Initalize a chess board and the possible moves of the knight.
        board = Board(8)
        dx = (2, 1, -1, -2, -2, -1, 1, 2)
        dy = (1, 2, 2, 1, -1, -2, -2, -1)
        # Holds the intermediate distance to the closer of the rook or queen.
        mid = None
        # Initialize queue and start node for BFS.
        Q = Queue()
        start = board[knight]
        start.visited = True
        start.d = 0
        Q.enqueue(start)
        while not Q.empty():
            u = Q.dequeue()
            i, j = u.i, u.j
            if (i, j) == rook or (i, j) == queen:
                if mid is not None:
                    # We're done.
                    return u.d + mid
                mid = u.d
                # Reset board and continue BFS till we find the other piece.
                board = Board(8)
                u = board[i, j]
                u.visited = True
                u.d = 0
                Q = Queue()
            for x, y in zip(dx, dy):
                v = board[i + x, j + y]
                if v is not None and not v.visited:
                    v.visited = True
                    v.d = u.d + 1
                    Q.enqueue(v)
        return -1

    def transform_to_coordinates(self, cr):
        return int(cr[1]) - 1, ord(cr[0]) - ord("a")


class Board(object):
    """Represents an nxn board."""
    def __init__(self, n):
        self.size = n
        self.board = [[Square(i, j) for j in xrange(n)] for i in xrange(n)]

    def __getitem__(self, index):
        row, col = index
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.board[row][col]
        return None

    def __setitem__(self, index, value):
        row, col = index
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = value


class Square(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False
        self.d = None


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
    # print CaptureThemAll().transform_to_coordinates("c5")
    print CaptureThemAll().fastKnight("a1", "b3", "c5")
    print CaptureThemAll().fastKnight("h8", "e2", "d2")
