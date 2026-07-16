class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            position = ord(c) - ord("a")
            if node.children[position] is None:
                node.children[position] = TrieNode()
            node = node.children[position]
        node.is_word_end = True

    def search(self, word: str) -> bool:
        return search(self.root, word, 0)


def search(node, word, position):
    if node is None:
        return False

    if position == len(word):
        return node.is_word_end

    c = word[position]
    if c == ".":
        for index in range(26):
            if search(node.children[index], word, position + 1):
                return True
        return False
    else:
        index = ord(c) - ord("a")
        return search(node.children[index], word, position + 1)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False
