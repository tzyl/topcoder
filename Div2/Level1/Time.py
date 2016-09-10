class Time(object):
    def whatTime(self, seconds):
        s = seconds % 60
        m = seconds % 3600 / 60
        h = seconds / 3600
        return "%s:%s:%s" % (h, m, s)

print Time().whatTime(86399)
