class Trienode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Trienode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.children.setdefault(ch,Trienode())
        cur.end = True
    
    def walk(self,s):
        cur = self.root
        for ch in s:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]
        return cur


    def search(self, word: str) -> bool:
        n = self.walk(word)
        return bool(n and n.end)

    def startsWith(self, prefix: str) -> bool:
        return self.walk(prefix) is not None
        