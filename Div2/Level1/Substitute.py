class Substitute(object):
    def getValue(self, key, code):
        key_map = {c: str((i + 1) % 10) for i, c in enumerate(key)}
        return int("".join(key_map[c] for c in code if c in key_map))
