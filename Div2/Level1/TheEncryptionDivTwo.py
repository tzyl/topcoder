class TheEncryptionDivTwo(object):
    # O(n) solution.
    def encrypt(self, message):
        cipher = {}
        encrypted = []
        for c in message:
            if c not in cipher:
                cipher[c] = chr(ord("a") + len(cipher))
            encrypted.append(cipher[c])
        return "".join(encrypted)

if __name__ == '__main__':
    print TheEncryptionDivTwo().encrypt("hello")
