import re
import typing as t


class RowModifier:
    def __init__(self) -> None:
        self._words_list: t.List = []
        self._shortest_words: t.List = []
        self._longest_words: t.List = []

    def add_sentence(self, sentence: str) -> t.List:
        punctuation_cleaning = re.sub(r"\W", " ", sentence).split()
        self._words_list.extend(punctuation_cleaning)
        for word in punctuation_cleaning:
            if len(word) == len(min(punctuation_cleaning, key=len)):
                self._shortest_words.append(word)
            elif len(word) == len(max(punctuation_cleaning, key=len)):
                self._longest_words.append(word)

    @property
    def view_shortest_words(self) -> t.List:
        return self._shortest_words

    @property
    def view_longest_words(self) -> t.List:
        return self._longest_words

    @property
    def view_sentence(self) -> t.List:
        return self._words_list

    def delete_word(self, word: str) -> t.List:
        return [x for x in self._words_list if x not in word.split()]
