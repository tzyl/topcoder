class Stitch(object):
    def stitch(self, A, B, overlap):
        if overlap == 0:
            return map(lambda x: x[0] + x[1], zip(A, B))

        stitched_rows = []
        for row1, row2 in zip(A, B):
            start, row1_overlap = row1[:-overlap], row1[-overlap:]
            row2_overlap, end = row2[:overlap], row2[overlap:]
            middle = "".join(self.merge(i, c1, c2, overlap) for i, (c1, c2) in enumerate(zip(row1_overlap, row2_overlap)))
            # print start, middle, end
            stitched_rows.append(start + middle + end)
        return stitched_rows

    def merge(self, i, c1, c2, overlap):
        return chr(int(round(float((overlap - i)*ord(c1) + (i + 1)*ord(c2)) / (overlap + 1))))

print Stitch().stitch([" 32ygfd", "3uh53G:", ")O83gh3"], ["hsd$*(PH", "3G:$)(*P", "gh86$PBB"], 3)
