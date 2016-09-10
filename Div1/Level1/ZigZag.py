class ZigZag(object):
    def longestZigZag(self, sequence):
        longest_sequence = []
        parity = []
        for i, num in enumerate(sequence):
            longest_sequence.append(1)
            parity.append(None)
            for j in xrange(i):
                if longest_sequence[j] + 1 > longest_sequence[i]:
                    if sequence[i] != sequence[j]:
                        direction = num > sequence[j]
                        if parity[j] is not direction:
                            longest_sequence[i] = longest_sequence[j] + 1
                            parity[i] = direction
        return max(longest_sequence)

print ZigZag().longestZigZag([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244])
