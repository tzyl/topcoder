class HuffmanDecoding(object):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def decode(self, archive, dictionary):
        if not archive:
            return ""
        for i, bit_string in enumerate(dictionary):
            if archive.startswith(bit_string):
                return self.alphabet[i] + self.decode(archive[len(bit_string):], dictionary)
