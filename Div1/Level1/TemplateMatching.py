# In this problem you will be given a text and you will need to find the substring of the text that matches a given template in the best way. The template will be represented by two s: prefix and suffix. Consider a string S. The prefix match score of S with respect to a given template is the maximal n >= 0 such that the first n characters of S are equal to the last n characters of prefix and occur in the same exact order. Analogously, the suffix match score of S is the maximal m >= 0 such that the last m characters of S are equal to the first m characters of suffix and occur in the same exact order.
# For example, if S = "something", prefix = "awesome", and suffix = "ingenious", than the prefix score of S is 4 (the matched characters are "some") and the suffix score is 3 (the matched characters are "ing").
# The match score of a string S with respect to a given template is the sum of its prefix and suffix match scores. Find the non-empty substring of text with the maximal match score according to the template (prefix, suffix). In case of a tie, return the substring with the maximal prefix score. If there are still several candidates, return one that comes first lexicographically.


class TemplateMatching(object):
    def bestMatch(self, text, prefix, suffix):
        result = ""
        best_prefix_score = -1
        best_suffix_score = -1
        for i in xrange(len(text)):
            for j in xrange(i, len(text)):
                s = text[i:j+1]
                a = min(len(prefix), len(s))
                while a > 0:
                    if s.startswith(prefix[-a:]):
                        break
                    a -= 1
                b = min(len(suffix), len(s))
                while b > 0:
                    if s.endswith(suffix[:b]):
                        break
                    b -= 1
                if (a + b > best_prefix_score + best_suffix_score or
                    a + b == best_prefix_score + best_suffix_score and
                    (a > best_prefix_score or a == best_prefix_score and
                        s < result)):
                    result = s
                    best_prefix_score = a
                    best_suffix_score = b
        return result

    # Somewhere not working?
    def bestMatch2(self, text, prefix, suffix):
        P = [[0] * len(text) for _ in xrange(len(text))]
        S = [[0] * len(text) for _ in xrange(len(text))]
        for i in xrange(len(text)):
            for j in xrange(i, len(text)):
                P[i][j] = self.longest_prefix_length(text[i:j+1], prefix)
                S[i][j] = self.longest_suffix_length(text[i:j+1], suffix)
        for row in P:
            print row
        print
        for row in S:
            print row
        best_score = 0
        best_candidates = []
        for i in xrange(len(text)):
            for j in xrange(i, len(text)):
                total = P[i][j] + S[i][j]
                if total > best_score:
                    best_score = total
                    best_candidates = [(i, j)]
                elif total == best_score:
                    best_candidates.append((i, j))
        print best_score
        print best_candidates
        if len(best_candidates) == 1:
            i, j = best_candidates[0][0], best_candidates[0][1]
            return text[i:j+1]
        best_prefix_score = 0
        best_prefix_candidates = []
        for candidate in best_candidates:
            i, j = candidate[0], candidate[1]
            if P[i][j] > best_prefix_score:
                best_prefix_score = P[i][j]
                best_prefix_candidates = [(i, j)]
            elif P[i][j] == best_prefix_score:
                best_prefix_candidates.append((i, j))
        best_prefix_candidates = [text[c[0]:c[1]+1] for c in best_prefix_candidates]
        best_prefix_candidates.sort()
        print best_prefix_score
        print best_prefix_candidates
        return best_prefix_candidates[0]

    def longest_prefix_length(self, text, prefix):
        for i in xrange(len(prefix) + 1):
            if text.startswith(prefix[i:]):
                return len(prefix) - i

    def longest_suffix_length(self, text, suffix):
        for i in reversed(xrange(len(suffix) + 1)):
            if text.endswith(suffix[:i]):
                return i

if __name__ == '__main__':
    import re
    pattern = re.compile("\"(.*?)\"")
    # print TemplateMatching().bestMatch("something", "awesome", "ingenious")
    # print TemplateMatching().bestMatch("mississippi", "promise", "piccolo")
    # print TemplateMatching().bestMatch("ab", "b", "a")
    # This case is wrong?
    # print TemplateMatching().bestMatch2('wrr zzo qt hgm rpneh awte o pcjvaa rb axgu cx', 'yigx e wpujledx ohut a ey v de lkzt x juvl', 'h ke rjpskpidwbg zojhc rsdjsi hobbxglyr rp tgh a ')
    # print ' zzo qt hgm rpneh '
    print TemplateMatching().bestMatch('wrr zzo qt hgm rpneh awte o pcjvaa rb axgu cx', 'yigx e wpujledx ohut a ey v de lkzt x juvl', 'h ke rjpskpidwbg zojhc rsdjsi hobbxglyr rp tgh a ')
    print TemplateMatching().bestMatch2('wrr zzo qt hgm rpneh awte o pcjvaa rb axgu cx', 'yigx e wpujledx ohut a ey v de lkzt x juvl', 'h ke rjpskpidwbg zojhc rsdjsi hobbxglyr rp tgh a ')
    # print TemplateMatching().bestMatch("wrr zzo qt hgm rpneh awte o pcjvaa rb axgu cx", " zzo qt hgm rpneh awte o pcjvaa rb axgu cx", "wrr zzo qt hgm rpneh awte o pcjvaa rb axgu")
