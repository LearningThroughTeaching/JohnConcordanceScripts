
class GreekWord:

    def __init__(self, greek_word, english_text, chapter, verse, word_index, i, fisher_section, strongs_number, strongs_word, strongs_data):
        """
         Creates a Greek Word using data available from the _concordance.json (plus dictionary file optional addition).
         """
        self.greek_word = greek_word.rstrip(",")
        self.english_text = english_text
        self.chapter = chapter
        self.verse = verse
        self.word_index = word_index
        self.i = i  # In the concordance data there is a field i which is almost word_index
        # However, if the same word appears later in the verse, then i becomes that later word_index (ugh)
        self.fisher_section = fisher_section
        self.strongs_number = strongs_number
        self.strongs_word = strongs_word  # Unused at present
        self.strongs_data = strongs_data  # Unused at present

    @property
    def verse_index(self):
        return f"{self.chapter}:{self.verse}.{self.word_index}"

    def __repr__(self):
        return f"{self.greek_word} - {self.english_text} ({self.chapter}:{self.verse}.{self.word_index}) {self.strongs_number} T{self.fisher_section}"
