# The Centaur company has N servers, numbered 1 through N. These servers
# are currently connected into a network. The topology of the network is a
# tree. In other words, there are exactly N-1 bidirectional cables, each
# connecting some two servers in such a way that the entire network is
# connected.

# The Centaur company is about to split into two new companies: the Human
# company and the Horse company. When this happens, the companies will
# divide the servers somehow. Once they divide their servers, they will
# cut each cable that connects a server of the Horse company and a server
# of the Human company.

# While the Horse company has a lot of cables, the Human company does not
# have any. Therefore, when dividing the servers, the Human company must
# get a set of servers that will remain connected after the cables are
# cut.

# You are given two s a and b, each containing N-1 elements. These two
# arrays describe the original cables: for each i, there is a cable that
# connects the servers a[i] and b[i].

# Compute and return the number of different ways in which the two
# companies may divide the servers. (It is possible that one of the
# companies will get no servers at all.)


def memoize(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper


# O(n) solution as a tree has O(n) edges.
class CentaurCompanyDiv2(object):
    def count(self, a, b):
        # DFS to build rooted structure of tree. Choose server 1 to be the
        # root (could have been any).
        n = len(a) + 1
        nodes = [TreeNode(i + 1) for i in xrange(n)]
        nodes[0].parent = nodes[0]
        stack = [nodes[0]]
        while stack:
            root = stack.pop()
            for i in xrange(len(a)):
                other = None
                if a[i] == root.index:
                    other = nodes[b[i] - 1]
                elif b[i] == root.index:
                    other = nodes[a[i] - 1]
                if other is not None and other is not root.parent:
                    # Found an edge to follow.
                    root.children.append(other)
                    other.parent = root
                    stack.append(other)
        # Add 1 because we do not count the empty subtree.
        return 1 + self.count_subtrees(nodes[0], False)

    # Recursively calculates how many subtrees there are depending on whether
    # the root must be used or not in the subtree.
    @memoize
    def count_subtrees(self, root, must_use_root):
        if must_use_root:
            count = 1
            for child in root.children:
                # For each child's subtrees which include the child, we can
                # either include the subtree or not.
                # Add 1 to account for empty subtree.
                count *= 1 + self.count_subtrees(child, True)
        else:
            count = 0
            # Decide to use the root in the subtree.
            count += self.count_subtrees(root, True)
            # Decide not to use the root in the subtree so we must use a
            # child's subtree.
            count += sum(self.count_subtrees(child, False) for child in root.children)
        return count


class TreeNode(object):
    def __init__(self, index):
        self.index = index
        self.parent = None
        self.children = []


if __name__ == '__main__':
    print CentaurCompanyDiv2().count(
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51])
