import json


class GreekWord:

    def __init__(self, greek_word, english_text, chapter, verse, word_index, fisher_teaching, strongs_number, strongs_word, strongs_data):
        """
         Creates a Greek Word using data available from the james.json plus dictionary file.
         """
        self.greek_word = greek_word
        self.english_text = english_text
        self.chapter = chapter
        self.verse = verse
        self.word_index = word_index
        self.fisher_teaching = fisher_teaching
        self.strongs_number = strongs_number
        self.strongs_word = strongs_word
        self.strongs_data = strongs_data

    @property
    def verse_index(self):
        return f"{self.chapter}:{self.verse}.{self.word_index}"

    def __repr__(self):
        return f"{self.greek_word} - {self.english_text} ({self.chapter}:{self.verse}.{self.word_index}) {self.strongs_number} T{self.fisher_teaching}"


def main():
    print("--- James Concordance ---")
    all_words = load_james()

    # find_strongs(all_words, ["g3956"], print_only=True) # All
    # find_strongs(all_words, ["g79", "g80"], print_only=True)  # adelphos
    # find_strongs(all_words, ["g5046", "g5055", "g5056"], print_only=True)  # adelphos
    # find_strongs(all_words, ["g5046", "g5055", "g5056", "g658", "g5048"], print_only=True)  # adelphos + bonus
    # find_strongs(all_words, ["g5046", "g5055", "g5056"], print_only=True)  # adelphos
    # find_strongs(all_words, ["g3648", "g3650"], print_only=True)  # Whole
    # find_strongs(all_words, ["g3986"], print_only=True)  # Trials
    # find_strongs(all_words, ["g3985"], print_only=True)  # Temptations (1)
    # find_strongs(all_words, ["g551"], print_only=True)  # Temptations (2)
    # find_strongs(all_words, ["g5278", "g5281" ], print_only=True)  # Perseverance
    # find_strongs(all_words, ["g3985"], print_only=True)  # Perseverance
    # find_strongs(all_words, ["g1097"], print_only=True)  # Knowing ginosko
    find_strongs(all_words, ["g1492"], print_only=True)  # Knowing eido

    print_range(all_words, start_ch=1, start_v=19)
    # print_range(all_words, start_ch=1, start_v=2, end_ch=1, end_v=4)
    #print_teaching(all_words, 2.1)


def print_range(all_words: list[GreekWord], start_ch, start_v, end_ch=None, end_v=None):
    if end_ch is None:
        end_ch = start_ch
    if end_v is None:
        end_v = start_v
    start_id = start_ch * 1000 + start_v
    end_id = end_ch * 1000 + end_v
    for word in all_words:
        verse_id = word.chapter * 1000 + word.verse
        if start_id <= verse_id <= end_id:
            print(word)


def print_teaching(all_words: list[GreekWord], teaching):
    for word in all_words:
        if word.fisher_teaching == teaching:
            print(word)


def load_james():
    james_json_file = open("james.json")

    verse_maps = json.load(james_json_file)
    greek_words = []

    for single_verse in verse_maps:
        current_chapter = int(single_verse["id"][2:5])
        current_verse = int(single_verse["id"][5:])
        current_fisher_teaching = get_fisher_teaching(current_chapter, current_verse)
        words = single_verse["verse"]

        for json_word in words:
            greek_word = json_word["word"]
            english_text = json_word["text"]
            # chapter = chapter
            # verse = verse
            word_index = json_word["i"]
            # fisher_teaching = fisher_teaching
            strongs_number = json_word["number"]
            # strongs_word = strongs_word
            # strongs_data = strongs_data
            greek_word = GreekWord(greek_word, english_text, current_chapter, current_verse, word_index, current_fisher_teaching, strongs_number, None, None)
            greek_words.append(greek_word)

    james_json_file.close()
    return greek_words


def find_strongs(all_words: list[GreekWord], strongs_list, print_only=True):
    greek_word_matches = []
    hits = 1
    prior_verse_index = None
    for word in all_words:
        found = False
        for strongs_number in strongs_list:
            if strongs_number in word.strongs_number and word.verse_index != prior_verse_index:
                found = True
                prior_verse_index = word.verse_index
        if found:
            if print_only:
                print(f"{hits}. {word}")
                hits += 1
            else:
                greek_word_matches.append(word)
    return greek_word_matches


def find_matches(all_words: list[GreekWord], regex_matches, print_only=True):
    greek_word_matches = []
    hits = 1
    for word in all_words:
        found = False
        for match in regex_matches:
            if match in word.greek_word.lower():
                found = True
        if found:
            if print_only:
                print(f"{hits}. {word}")
                hits += 1
            else:
                greek_word_matches.append(word)
    return greek_word_matches


def get_fisher_teaching(chapter, verse):
    if chapter == 1:
        if verse == 1:
            return 0.1
        elif verse <= 4:
            return 1.1
        elif verse <= 8:
            return 1.2
        elif verse <= 12:  # Previously 11
            return 1.3
        elif verse <= 18:
            return 1.4
        elif verse <= 21:
            return 2.1
        elif verse <= 25:
            return 2.2
        else:
            return 2.3
    elif chapter == 2:
        if verse <= 13:
            return 3.1
        else:
            return 3.2
    elif chapter == 3:
        if verse <= 12:
            return 3.3
        else:
            return 3.4
    elif chapter == 4:
        if verse <= 10:
            return 4.1
        elif verse <= 12:
            return 4.2
        else:
            return 4.3
    elif chapter == 5:
        if verse <= 11:
            return 5.1
        elif verse == 12:
            return 5.2
        elif verse <= 18:
            return 5.3
        else:
            return 5.4


if __name__ == "__main__":
    main()
