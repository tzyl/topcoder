class Traffic(object):
    def time(self, lights, speed):
        time = 150.0 / speed
        for light in lights:
            if time / light % 2 >= 1:
                # Hit a red light, wait till green.
                time = time - (time % light) + light
            time += 150.0 / speed
        return int(time)
