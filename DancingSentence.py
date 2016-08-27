class DancingSentence(object):
    def makeDancing(self, sentence):
        dancing_sentence = []
        uppercase = True
        for c in sentence:
            if c == " ":
                dancing_sentence.append(c)
            else:
                if c.isupper() is uppercase:
                    dancing_sentence.append(c)
                else:
                    dancing_sentence.append(c.lower() if c.isupper() else c.upper())
                uppercase = not uppercase
        return "".join(dancing_sentence)

print DancingSentence().makeDancing(" This is a dancing sentence ")
