class TallPeople(object):
    def getPeople(self, people):
        people = [map(int, row.split()) for row in people]
        tallest_of_shortest = 0
        for row in people:
            tallest_of_shortest = max(tallest_of_shortest, min(row))
        shortest_of_tallest = float("inf")
        for j in xrange(len(people[0])):
            shortest_of_tallest = min(shortest_of_tallest,
                                      max(row[j] for row in people))
        return (tallest_of_shortest, shortest_of_tallest)

if __name__ == '__main__':
    print TallPeople().getPeople(["9 2 3", "4 8 7"])
