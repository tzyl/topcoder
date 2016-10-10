from itertools import combinations


class BridgeCrossing(object):
    def minTime(self, times):
        return self._minTime(times, [])

    def _minTime(self, times, across):
        if len(times) <= 2:
            return max(times)
        best = float("inf")
        # Try each pair of people as the starting pair.
        for pair in combinations(times, 2):
            total = max(pair)
            # Create copy of list so we can modify it and pass along.
            new_times = list(times)
            new_across = list(across)
            # Move the pair across the bridge and the fastest one across back.
            new_times.remove(pair[0])
            new_times.remove(pair[1])
            new_across.append(pair[0])
            new_across.append(pair[1])
            x = min(new_across)
            new_across.remove(x)
            new_times.append(x)
            total += x
            # Recursively get the next best choice if it is a candidate.
            if total < best:
                total += self._minTime(new_times, new_across)
            best = min(best, total)
        return best

if __name__ == '__main__':
    print BridgeCrossing().minTime([1, 2, 5, 10])
    print BridgeCrossing().minTime([1, 2, 3, 50, 99, 100])
