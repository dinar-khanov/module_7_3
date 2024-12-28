class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in punctuation:
                        content = content.replace(punct, '')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                results[name] = words.index(word) + 1  # 1-based index
            else:
                results[name] = None
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            results[name] = words.count(word)
        return results

# Example usage
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))