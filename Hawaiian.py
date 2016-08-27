class Hawaiian(object):
    hawaiian_alphabet = set("aeiouhklmnpw")

    def getWords(self, sentence):
        words = sentence.split()
        valid_words = [word for word in words if self.is_valid_hawaiian(word)]
        return valid_words

    def is_valid_hawaiian(self, word):
        for c in word:
            if c.lower() not in self.hawaiian_alphabet:
                return False
        return True

print Hawaiian().getWords("Mauna Kea and Mauna Koa are two mountains")
