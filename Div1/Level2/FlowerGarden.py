class FlowerGarden(object):
    # Nice Python solution
    def getOrdering(self, height, bloom, wilt):
        flowers = zip(height, bloom, wilt)
        flowers.sort()

        def flowersOverlap(f1, f2):
            # Overlap if each blooms before the other wilts.
            return f2[1] <= f1[2] and f1[1] <= f2[2]

        rows = []
        for flower in flowers:
            rowIndex = len(rows)
            # Start at the back and move forward if not overlapping.
            while rowIndex > 0 and not flowersOverlap(flower, rows[rowIndex - 1]):
                rowIndex -= 1
            # rows[rowIndex:rowIndex] = [flower]
            rows.insert(rowIndex, flower)

        return [flower[0] for flower in rows]

    # More generic solution
    def getOrdering2(self, height, bloom, wilt):
        n = len(height)
        done = [False] * n
        result = []

        def invalid(i):
            for j in xrange(n):
                if not done[j] and height[j] < height[i]:
                    if bloom[i] <= wilt[j] and bloom[j] <= wilt[i]:
                        # i won't work here so skip to next.
                        return True
            return False

        for _ in xrange(n):
            best = -1
            best_h = -1
            for i in xrange(n):
                if not done[i] and height[i] > best_h:
                    if invalid(i):
                        continue
                    best = i
                    best_h = height[best]
            done[best] = True
            result.append(best_h)

        return result

# print FlowerGarden().getOrdering([5, 4, 3, 2, 1], [1, 1, 1, 1, 1], [365, 365, 365, 365, 365])
# print FlowerGarden().getOrdering([5, 4, 3, 2, 1], [1, 5, 10, 15, 20], [4, 9, 14, 19, 24])
# print FlowerGarden().getOrdering([5, 4, 3, 2, 1], [1, 5, 10, 15, 20], [5, 10, 15, 20, 25])
# print FlowerGarden().getOrdering([5, 4, 3, 2, 1], [1, 5, 10, 15, 20], [5, 10, 14, 20, 25])
# print FlowerGarden().getOrdering([1, 2, 3, 4, 5, 6], [1, 3, 1, 3, 1, 3], [2, 4, 2, 4, 2, 4])
# print FlowerGarden().getOrdering([3, 2, 5, 4], [1, 2, 11, 10], [4, 3, 12, 13])
print FlowerGarden().getOrdering([776, 826, 521, 242, 807, 565, 945, 606, 149, 698, 609, 857, 894, 234, 997, 382, 512, 43, 186, 504, 264, 878, 271, 143, 199, 973, 321, 126, 653, 819, 518, 901, 797, 57, 301, 975, 934, 209, 865, 983, 491, 67, 680, 828, 834], [29, 94, 166, 68, 161, 279, 35, 135, 145, 257, 139, 108, 224, 102, 217, 195, 282, 217, 178, 308, 186, 156, 87, 229, 112, 193, 328, 142, 79, 301, 114, 351, 74, 48, 264, 55, 184, 60, 323, 59, 293, 16, 212, 7, 63], [184, 150, 275, 150, 197, 333, 199, 292, 247, 312, 162, 225, 279, 104, 362, 285, 304, 344, 320, 352, 288, 204, 88, 344, 251, 337, 338, 180, 263, 341, 340, 355, 220, 207, 346, 135, 257, 186, 342, 340, 320, 265, 292, 344, 174])
