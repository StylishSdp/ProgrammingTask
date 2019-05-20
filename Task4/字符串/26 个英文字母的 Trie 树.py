class TrieTree:
    def __init__(self):
        self.root = {}
        self.word_end = -1

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.word_end] = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False
            current = current[c]

        if self.word_end not in current:
            return False
        return True

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True