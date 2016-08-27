class Unblur(object):
    def original(self, blurred):
        self.blurred = [map(int, list(row)) for row in blurred]
        self.unblurred = [["."] * len(blurred[0]) for _ in xrange(len(blurred))]

        for i in xrange(1, len(blurred) - 1):
            for j in xrange(1, len(blurred[0]) - 1):
                if self.blurred[i-1][j-1]:
                    self.unblurred[i][j] = "#"
                    self.decrement_blurred_neighbours(i, j)

        return ["".join(row) for row in self.unblurred]

    def decrement_blurred_neighbours(self, i, j):
        # print "DECREMENT NEIGHBOURS OF %s,%s" % (i, j)
        for x in xrange(max(i - 1, 0), min(i + 2, len(self.unblurred))):
            for y in xrange(max(j - 1, 0), min(j + 2, len(self.unblurred[0]))):
                self.blurred[x][y] -= 1


class Unblur2(object):
    def original(self, blurred):
        # Make blurred a list of lists.
        self.blurred = [map(int, list(row)) for row in blurred]
        self.neighbour_counts = [[0] * len(blurred[0]) for _ in xrange(len(blurred))]
        self.unblurred = [[0] * len(blurred[0]) for _ in xrange(len(blurred))]

        self.dont_call_on = [[0] * len(blurred[0]) for _ in xrange(len(blurred))]

        self.recount_neighbours()
        # self.show_board()

        iteration = 1
        # print "STARTING ITERATIONS"
        while any(self.neighbour_counts[i][j] for i, j in self.index_generator()):
            # print str(iteration) + " here"

            # start = time.time()
            for i, j in self.index_generator():
                if self.blurred[i][j] == 0 and not self.dont_call_on[i][j]:
                    # print "MARK NEIGHBOURS OF %s,%s BLACK" % (i, j)
                    self.mark_neighbours(i, j, "black")
                    self.dont_call_on[i][j] = 1
            # print time.time() - start

            # start = time.time()
            for i, j in self.index_generator():
                if self.blurred[i][j] > 0 and self.blurred[i][j] == self.neighbour_counts[i][j]:
                    # print "MARK NEIGHBOURS OF %s,%s WHITE" % (i, j)
                    self.mark_neighbours(i, j, "white")
            # print time.time() - start

            # start = time.time()
            for i, j in self.index_generator():
                down = (i+1, j)
                # up = (i-1, j)
                right = (i, j+1)
                # left = (i, j-1)
                # directions = [down, up, right, left]
                directions = [down, right]

                for i2, j2 in directions:
                    try:
                        if not (self.dont_call_on[i][j] or self.dont_call_on[i2][j2]):
                            self.deduce_from_difference(i, j, i2, j2)
                    except:
                        continue
            # print time.time() - start

            # self.show_board()
            iteration += 1

        # print iteration - 1

        return ["".join(row) for row in self.unblurred]


    def deduce_from_difference(self, i, j, i2, j2):
        coords = self.get_neighbour_coordinates(i, j)
        neighbour_coords = self.get_neighbour_coordinates(i2, j2)

        left_behind = [coord for coord in coords if coord not in neighbour_coords]

        if not all(self.unblurred[i][j] == "." for i, j in left_behind):
            # print "Not all black, return"
            return

        new_uninitialized = [coord for coord in neighbour_coords if coord not in coords if self.unblurred[coord[0]][coord[1]] == 0]
        difference = self.blurred[i2][j2] - self.blurred[i][j]
        if difference == 0:
            for i, j in new_uninitialized:
                self.unblurred[i][j] = "."
        elif difference > 0 and difference == len(new_uninitialized):
            for i, j in new_uninitialized:
                self.unblurred[i][j] = "#"
                self.decrement_blurred_neighbours(i, j)
        self.recount_neighbours()
        # self.show_board()

    def get_neighbour_coordinates(self, i, j):
        coords = []
        for x in xrange(max(i - 1, 0), min(i + 2, len(self.blurred))):
            for y in xrange(max(j - 1, 0), min(j + 2, len(self.blurred[0]))):
                coords.append((x, y))
        return coords

    def mark_neighbours(self, i, j, colour):
        for x in xrange(max(i - 1, 0), min(i + 2, len(self.blurred))):
            for y in xrange(max(j - 1, 0), min(j + 2, len(self.blurred[0]))):
                if self.unblurred[x][y] == 0:
                    if colour == "black":
                        self.unblurred[x][y] = "."
                    elif colour == "white":
                        self.unblurred[x][y] = "#"
                        self.decrement_blurred_neighbours(x, y)
        self.recount_neighbours()
        # self.show_board()


    def decrement_blurred_neighbours(self, i, j):
        # print "DECREMENT NEIGHBOURS OF %s,%s" % (i, j)
        for x in xrange(max(i - 1, 0), min(i + 2, len(self.unblurred))):
            for y in xrange(max(j - 1, 0), min(j + 2, len(self.unblurred[0]))):
                self.blurred[x][y] -= 1

    def recount_neighbours(self):
        for i, j in self.index_generator():
            self.neighbour_counts[i][j] = self.count_neighbours_left(i, j)

    def count_neighbours_left(self, i, j):
        count = 0
        for x in xrange(max(i - 1, 0), min(i + 2, len(self.unblurred))):
            for y in xrange(max(j - 1, 0), min(j + 2, len(self.unblurred[0]))):
                if self.unblurred[x][y] == 0:
                    count += 1
        return count

    def index_generator(self):
        for i in xrange(len(self.blurred)):
            for j in xrange(len(self.blurred[0])):
                yield i, j

    def show_board(self):
        print "CURRENT BLURRED:"
        for row in self.blurred:
            print row
        print "CURRENT NEIGHBOUR COUNTS:"
        for row in self.neighbour_counts:
            print row
        print "CURRENT UNBLURRED:"
        for row in self.unblurred:
            print row
        print "\n"

cls = Unblur()
for row in cls.original(["1233321000000000123332100000000000000000000", "1244422233222332334343323322232112332223321", "1255523344343443545343434434343233432334432", "0033303455465775633011445546454355753457753", "0033303333364543533011433336333364521346542", "0033303455464532445343545546454355753446542", "0022202344342200234343434434343233432323221", "0011101233221100123332223322232112332211111"]):
    print row
