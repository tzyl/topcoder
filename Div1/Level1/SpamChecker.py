class SpamChecker(object):
    def spamCheck(self, judgeLog, good, bad):
        score = 0
        for line in judgeLog:
            if line == "o":
                score += good
            elif line == "x":
                score -= bad
            if score < 0:
                return "SPAM"
        return "NOT SPAM"
