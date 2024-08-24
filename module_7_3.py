class WordsFinder:
    file_names = []

    def __init__(self, *filenames):
        for i in filenames:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for filename in self.file_names:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()
                words = [word for word in text.lower().split()]
                for i in punct:
                    for j in range(len(words)):
                        words[j] = words[j].replace(i, '')
                all_words[filename] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            index = words.index(word)
            index += 1
            result[name] = index
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            counts = words.count(word)
            result[name] = counts
        return result


if __name__ == "__main__":
    finder2 = WordsFinder('product.txt')
    print(finder2.get_all_words())
    print(WordsFinder.file_names)
    print(finder2.find('potato'))
    print(finder2.count('potato'))
