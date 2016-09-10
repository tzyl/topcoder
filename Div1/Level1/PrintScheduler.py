class PrintScheduler(object):
    def getOutput(self, threads, slices):
        thread_indexes = [0] * len(threads)
        output = []
        for time_slice in slices:
            thread, time = map(int, time_slice.split())
            for _ in xrange(time):
                output.append(threads[thread][thread_indexes[thread]])
                thread_indexes[thread] = (thread_indexes[thread] + 1) % len(threads[thread])
        return "".join(output)
