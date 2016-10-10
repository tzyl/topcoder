class UpDownHiking(object):
    def maxHeight(self, N, A, B):
        current_height = 0
        for i in xrange(N):
            can_go_up = (N - (i + 1)) * B > current_height
            if can_go_up:
                # Choose to ascend.
                current_height += min(A, (N - (i + 1)) * B - current_height)
            else:
                break
        return current_height

if __name__ == '__main__':
    print UpDownHiking().maxHeight(10, 10, 100)
