class RemoveCharacters(object):
    def minimalDistinct(self, A, B):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        checker = [0] * 26
        self.ans = 30

        def brute(pos, cur, mask):
            if pos == 26:
                self.ans = min(self.ans, cur)
                return
            brute(pos + 1, cur + 1, mask)
            nmask = mask & checker[pos]
            if (nmask >> pos) & 1:
                brute(pos + 1, cur, nmask)
            return

        for i, c in enumerate(alphabet):
            for j, d in enumerate(alphabet):
                a = ""
                b = ""
                for e in A:
                    if e == c or e == d:
                        a += e
                for e in B:
                    if e == c or e == d:
                        b += e
                if a == b:
                    checker[i] |= 1 << j
        brute(0, 0, (1 << 26) - 1)
        return self.ans

    def minimalDistinct4(self, A, B):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        checker = [0] * 26
        for i, c in enumerate(alphabet):
            for d in alphabet[i:]:
                a = ""
                b = ""
                for e in A:
                    if e == c or e == d:
                        a += e
                for f in B:
                    if f == c or f == d:
                        b += f
                if a != b:
                    checker[ord(c) - ord("a")] |= 1 << (ord(d) - ord("a"))
                    checker[ord(d) - ord("a")] |= 1 << (ord(c) - ord("a"))
        # print map(bin, checker)
        ans = 0
        for i in [1 << i for i in xrange(26)]:
            # print i
            if i.bit_length() <= ans:
                continue
            for j in xrange(26):
                if (i >> j) & 1 == 0:
                    continue
                if checker[j] & 1 != 0:
                    break
            else:
                ans = i.bit_length()
        return 26 - ans

    def minimalDistinct3(self, A, B):
        removed_chars = [[None] * (len(B) + 1) for _ in xrange(len(A) + 1)]
        # Initialize table when one string is of zero length.
        for i in xrange(len(A) + 1):
            removed_chars[i][0] = set(A[:i])
        for j in xrange(len(B) + 1):
            removed_chars[0][j] = set(B[:j])
        # Fill in table.
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                if A[i] == B[j]:
                    removed_chars[i + 1][j + 1] = removed_chars[i][j]
                # elif A[i] in removed_chars[i][j + 1]:
                #     removed_chars[i + 1][j + 1] = removed_chars[i][j + 1]
                # elif B[j] in removed_chars[i + 1][j]:
                #     removed_chars[i + 1][j + 1] = removed_chars[i + 1][j]
                else:
                    top = set(removed_chars[i][j + 1])
                    left = set(removed_chars[i + 1][j])
                    top.add(A[i])
                    left.add(B[j])
                    removed_chars[i + 1][j + 1] = min(top, left, key=len)
        # print "\n".join(str(row) for row in removed_chars)
        return len(removed_chars[len(A)][len(B)])

    # ~O(n^3)
    def minimalDistinct2(self, A, B):
        best = []
        # common_subsequences = set()

        def is_subsequence(subsequence, s):
            # if subsequence in common_subsequences:
            #     return True
            i = 0
            j = 0
            while i < len(subsequence) and j < len(s):
                if s[j] == subsequence[i]:
                    i += 1
                j += 1
            return i == len(subsequence)

        def number_distinct(subsequence, A, B):
            a, b = list(A), list(B)
            for c in subsequence:
                a.remove(c)
                b.remove(c)
            return len(set(a).union(set(b)))

        if len(A) != len(B):
            A, B = min(A, B, key=len), max(A, B, key=len)
        for i, c in enumerate(A):
            if c not in B:
                best.append("")
                continue
            best_here = c
            distinct = number_distinct(best_here, A, B)
            for subsequence in best:
                if number_distinct(subsequence + c, A, B) < distinct:
                    if is_subsequence(subsequence + c, B):
                        best_here = subsequence + c
                        # common_subsequences.add(best_here)
                        distinct = number_distinct(best_here, A, B)
            best.append(best_here)

        return min(number_distinct(subsequence, A, B) for subsequence in best)

    def longest_common_subsequence(self, s1, s2):
        """
        Uses dynamic programming to compute length of longest common
        subsequence of the two input strings s1 and s2.
        """
        lcs = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    lcs[i + 1][j + 1] = lcs[i][j] + 1
                else:
                    lcs[i + 1][j + 1] = max(lcs[i][j + 1], lcs[i + 1][j])
        return lcs[len(s1)][len(s2)]

        # Recursive relation. Could implement this with memoization.
        # if not s1 or not s2:
        #     return ""
        # if s1[-1] == s2[-1]:
        #     return self.longest_common_subsequence(s1[:-1], s2[:-1]) + s1[-1]
        # else:
        #     return max(self.longest_common_subsequence(s1[:-1], s2), self.longest_common_subsequence(s1, s2[:-1]), key=len)

    # ~O(n^3) solution
    def longest_common_subsequence2(self, s1, s2):
        longest = []
        common_subsequences = set()

        def is_subsequence(subsequence, s):
            if subsequence in common_subsequences:
                return True
            i = 0
            j = 0
            while i < len(subsequence) and j < len(s):
                if s[j] == subsequence[i]:
                    i += 1
                j += 1
            return i == len(subsequence)

        shorter, longer = min(s1, s2, key=len), max(s1, s2, key=len)
        for c in shorter:
            if c not in longer:
                longest.append("")
                continue
            longest_here = c
            for subsequence in longest:
                if len(subsequence + c) > len(longest_here):
                    if is_subsequence(subsequence + c, longer):
                        longest_here = subsequence + c
                        common_subsequences.add(longest_here)
            longest.append(longest_here)
        # print longest
        return max(longest, key=len)

# print RemoveCharacters().longest_common_subsequence("abc", "bacccc")
# print RemoveCharacters().longest_common_subsequence("a" * 1000, "a" * 1000)
# print RemoveCharacters().minimalDistinct("acabc", "accabcc")
print RemoveCharacters().minimalDistinct("mnopqrstuvwxyzabcdmnopqrstuvwxyzemfmmmmmgmhmmimjmkmmml", "abcdpopopefghijkl")
print RemoveCharacters().minimalDistinct("abacadaeafagahaiajakalamanaoapaqarasatauavawaxayazbcbdbebfbgbhbibjbkblbmbnbobpbqbrbsbtbubvbwbxbybzcdcecfcgchcicjckclcmcncocpcqcrcsctcucvcwcxcyczdedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzefegeheiejekelemeneoepeqereseteuevewexeyezfgfhfifjfkflfmfnfofpfqfrfsftfufvfwfxfyfzghgigjgkglgmgngogpgqgrgsgtgugvgwgxgygzhihjhkhlhmhnhohphqhrhshthuhvhwhxhyhzijikiliminioipiqirisitiuiviwixiyizjkjljmjnjojpjqjrjsjtjujvjwjxjyjzklkmknkokpkqkrksktkukvkwkxkykzlmlnlolplqlrlsltlulvlwlxlylzmnmompmqmrmsmtmumvmwmxmymznonpnqnrnsntnunvnwnxnynzopoqorosotouovowoxoyozpqprpsptpupvpwpxpypzqrqsqtquqvqwqxqyqzrsrtrurvrwrxryrzstsusvswsxsysztutvtwtxtytzuvuwuxuyuzvwvxvyvzwxwywzxyxzyz", "abacadaeafgaahaiajakalamanaoapaqarsaatuaavawaxyaazbcdbbebfbgbhbibjbklbbmnbbobpqbbrsbtbbuvbbwbxbybzcdcefcgcchcicjckclcmnccocpcqcrcsctcuvcwcxccyczeddfgddhiddjdkldmddndodpdqrddstddudvdwdxydzdefegheeiejekleemeneopeqeerseeteuevewexeyezgffhifjfkfflfmfnfofpfqfrfsftfufvfwfxfyfzghgigjgklgmggnoggpgqrgsgtguggvgwgxgyzgihhjhkhlmhnhohhpqhhrhshthuhvwhhxhyzhijikiliminioipiqirisitiuviiwxiiyzijkjljmnjojpjjqrjsjjtujjvjwxjjyjzklkmknokkpkqkrkstkkuvkwkkxkykzlmlnlolplqlrlsltlulvwlxlyllzmnmopmmqrmmsmtmumvmwmxymzmonnpqnrnnsntunvnnwxnnyznopoqroostouoovowoxyoozpqprpsptpupvwppxyppzrqqsqtuqqvwqxqqyzqrsrturvrrwrxryzrstsusvswsxyszstutvtwxtytztvuwuuxyuuzvwvxyvvzwxwywzyxxzyz")
print RemoveCharacters().minimalDistinct("abacadaeafagahaiajakalamanaoapaqarasatauavawaxayazbcbdbebfbgbhbibjbkblbmbnbobpbqbrbsbtbubvbwbxbybzcdcecfcgchcicjckclcmcncocpcqcrcsctcucvcwcxcyczdedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzefegeheiejekelemeneoepeqereseteuevewexeyezfgfhfifjfkflfmfnfofpfqfrfsftfufvfwfxfyfzghgigjgkglgmgngogpgqgrgsgtgugvgwgxgygzhihjhkhlhmhnhohphqhrhshthuhvhwhxhyhzijikiliminioipiqirisitiuiviwixiyizjkjljmjnjojpjqjrjsjtjujvjwjxjyjzklkmknkokpkqkrksktkukvkwkxkykzlmlnlolplqlrlsltlulvlwlxlylzmnmompmqmrmsmtmumvmwmxmymznonpnqnrnsntnunvnwnxnynzopoqorosotouovowoxoyozpqprpsptpupvpwpxpypzqrqsqtquqvqwqxqyqzrsrtrurvrwrxryrzstsusvswsxsysztutvtwtxtytzuvuwuxuyuzvwvxvyvzwxwywzxyxzyz", "bacaadeaafaghaiaajkalamaanoaapaqrasatauavawaxaayzacbdbebfbgbhbibbjkblbmbbnbobpbqrbsbtbubvbwbbxbyzbdceccfcghccicjkclcmccnocpccqcrcstccuvcwcxcyczcedfdgdhdidjdkdldmdnddopddqrddstdudvdwdxdyddzefegehiejekelemeneoeepqereesteueveweexyezefgfhifjffklfmfnffopfqfrffstffuvffwxffyzfhggijgkglgmgngogpggqrgsgtgguvgwgxgygzghihjhkhlmhnhohphqhrhshthuhvhwhxhyhzhijkilimiinoiipqirisitiuiiviwxiyizikjljmjnjjopjqjjrjsjtujvjwjjxyjzjlkmknkokpkqkrkskktukvkkwxkykkzmlnlolplqlrlsltllulvwlxlylzlnmmopmqmrmmsmtummvmwxmymmznonpqnrnnstnunvnwnxnynznpoqorosotouoovwooxyoozpqrpsptpupvpwpxpypzpqrsqqtquqvwqxqyqzqrstrrurvwrxryrzrtsusvsswsxysszutvtwttxtyztvuuwxuyuzuwvvxyvzvxwywzwxyzxzy")
