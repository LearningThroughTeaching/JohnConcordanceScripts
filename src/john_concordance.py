import json


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


def main():
    print("--- John Concordance ---")
    all_words = load_greek_concordance("john_concordance.json")

    # find_strongs(all_words, ["g3956"], print_only=True) # All
    # find_strongs(all_words, ["g79", "g80"], print_only=True)  # adelphos
    # find_strongs(all_words, ["g5046", "g5055", "g5056"], print_only=True)  # teleios
    # find_strongs(all_words, ["g5046", "g5055", "g5056", "g658", "g5048"], print_only=True)  # teleios + bonus
    # find_strongs(all_words, ["g5046", "g5055", "g5056"], print_only=True)  # adelphos
    # find_strongs(all_words, ["g3648", "g3650"], print_only=True)  # Whole
    # find_strongs(all_words, ["g3986"], print_only=True)  # Trials
    # find_strongs(all_words, ["g3985"], print_only=True)  # Temptations (1)
    # find_strongs(all_words, ["g551"], print_only=True)  # Temptations (2)
    # find_strongs(all_words, ["g5278", "g5281" ], print_only=True)  # Perseverance
    # find_strongs(all_words, ["g3985"], print_only=True)  # Perseverance
    # find_strongs(all_words, ["g1097"], print_only=True)  # Knowing ginosko
    # find_strongs(all_words, ["g1492"], print_only=True)  # Knowing eido

    # Interesting words:
    # Jews, water, testimony, witness, grace, Word (in caps in English),
    # Ginosko, telios (13:1),

    # Teleios
    # print("1. τέλειος - Perfect, mature, complete, whole")
    # print("----------------- starts with")
    # find_matches(all_words, ["τέλ", "τελ", "τετελε", "τετέλ"], starts_with_matches_only=True)
    # print("-----------------")
    # find_strongs(all_words, ["g5055", "g5056", "g5048"], print_only=True)  # teleios + bonus
    # print("-----------------")

    # print("2. ἀδελφὸς - Brothers or sisters")
    # find_matches(all_words, ["ἀδελφ", "αδελφ"])
    # find_strongs(all_words, ["g79", "g80"], print_only=True)  # adelphos
    # print("-----------------")

    # print("17. λόγῳ - Word")
    # print("-----------------")
    # find_matches(all_words, ["λόγ", "λόγου", "λόγῳ", "λόγον","λογ"], starts_with_matches_only=True)
    # print("-----------------")  # The on above finds the "spear" used to pierce his side
    # find_strongs(all_words, ["g3056"], print_only=True)  # word
    # print("-----------------")

    print("18. νομος - Law")
    find_matches(all_words, ["νομ", "νομο", "νόμο", "νόμ", "νόμό", "νομό"], starts_with_matches_only=True)
    print("-----------------")
    find_strongs(all_words, ["g3551"], print_only=True)  # word
    print("-----------------")

    # print_range(all_words, ch=18, v=28)
    # print_range(all_words, start_ch=1, start_v=2, end_ch=1, end_v=4)
    #print_section(all_words, 2.1)


def print_range(all_words: list[GreekWord], ch, v, end_ch=None, end_v=None):
    if end_ch is None:
        end_ch = ch
    if end_v is None:
        end_v = v
    start_id = ch * 1000 + v
    end_id = end_ch * 1000 + end_v
    for word in all_words:
        verse_id = word.chapter * 1000 + word.verse
        if start_id <= verse_id <= end_id:
            print(word)


def print_section(all_words: list[GreekWord], section):
    for word in all_words:
        if word.fisher_section == section:
            print(word)


def load_greek_concordance(concordance_filename):
    greek_concordance_json_file = open(f"../data/greek_concordances/{concordance_filename}")

    verse_maps = json.load(greek_concordance_json_file)
    greek_words = []

    for single_verse in verse_maps:
        current_chapter = int(single_verse["id"][2:5])
        current_verse = int(single_verse["id"][5:])
        current_fisher_section = get_fisher_section(current_chapter, current_verse)
        words = single_verse["verse"]

        word_index = 0
        for json_word in words:
            greek_word = json_word["word"]
            english_text = json_word["text"]
            # chapter = chapter
            # verse = verse
            i = json_word["i"]  # really not that useful, similar to word_index but different for repeated words (i becomes the final word_index)
            # fisher_section = fisher_section
            strongs_number = json_word["number"]
            # strongs_word = strongs_word
            # strongs_data = strongs_data
            greek_word = GreekWord(greek_word, english_text, current_chapter, current_verse, word_index, i, current_fisher_section, strongs_number, None, None)
            greek_words.append(greek_word)
            word_index += 1

    greek_concordance_json_file.close()
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


def find_matches(all_words: list[GreekWord], regex_matches, starts_with_matches_only=False, print_only=True):
    greek_word_matches = []
    hits = 1
    for word in all_words:
        found = False
        for match in regex_matches:
            if starts_with_matches_only:
                if word.greek_word.lower().startswith(match):
                    found = True
            else:
                if match in word.greek_word.lower():
                    found = True
        if found:
            if print_only:
                print(f"{hits}. {word}")
                hits += 1
            else:
                greek_word_matches.append(word)
    return greek_word_matches


def get_fisher_section(chapter, verse):
    if chapter == 1:
        if verse <= 19:
            return 1.1
        else:
            return 2.3
    else:
        return 2.0


if __name__ == "__main__":
    main()
