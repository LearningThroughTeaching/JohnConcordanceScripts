import json

RUN_ONCE = False
AUTO_SELECTION = None  # Note, do 1 less than the displayed prompt
USE_MOST_RECENT_SEARCH = False


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


class StrongWord:

    def __init__(self, dict_blob):
        self.word = dict_blob["word"]
        self.number = dict_blob["strongs"]
        self.data = StrongsData(dict_blob["data"])

    def __repr__(self):
        return f"Dictionary info: {self.number} - {self.word} {self.data}"


class StrongsData:

    def __init__(self, data_blob):
        self.comment = ""
        if "comment" in data_blob:
            self.comment = data_blob["comment"]

        self.see = ""
        if "see" in data_blob:
            self.see = data_blob["see"]

        self.deriv = ""
        if "deriv" in data_blob:
            self.deriv = data_blob["deriv"]

        self.defs_short = []
        self.defs_long = []
        if "def" in data_blob:
            defs = data_blob["def"]
            if "short" in defs:
                if isinstance(defs["short"], str):
                    self.defs_short = [defs["short"]]
                elif isinstance(defs["short"], list):
                    self.defs_short = defs["short"]
            if "long" in defs:
                if isinstance(defs["long"], str):
                    self.defs_long = [defs["long"]]
                elif isinstance(defs["long"], list):
                    self.defs_long = defs["long"]

    def pretty_list(self, title, list_prop):
        if len(list_prop) == 0:
            return ""
        if isinstance(list_prop, str):
            return "\n  " + title + list_prop
        if len(list_prop) == 1:
            return "\n  " + title + list_prop[0]
        list_str = "\n  " + title
        for item in list_prop:
            list_str += "\n    " + str(item)
        return list_str

    def __repr__(self):
        display_str = ""
        display_str += self.pretty_list("See - ", self.see)
        display_str += self.pretty_list("Derived from - ", self.deriv)
        display_str += self.pretty_list("Comment - ", self.comment)
        display_str += self.pretty_list("Def Short - ", self.defs_short)
        display_str += self.pretty_list("Def Long - ", self.defs_long)
        return display_str


class WordSearchOptions:

    def __init__(self, title, string_matches, strong_numbers):
        self.title = title
        self.string_matches = string_matches
        self.strong_numbers = strong_numbers
        self.starts_with_matches_only = True

    def __repr__(self):
        return self.title


def main():
    print("--- James and John Concordance Comparisons ---")
    james_words = load_greek_concordance("james_concordance.json")
    john_words = load_greek_concordance("john_concordance.json")
    john_1_words = load_greek_concordance("1_john_concordance.json")
    john_2_words = load_greek_concordance("2_john_concordance.json")
    john_3_words = load_greek_concordance("3_john_concordance.json")
    revelation_words = load_greek_concordance("revelation_concordance.json")

    greek_dictionary_map = load_dictionary("greek.json")

    # Teleios
    three_word_banks = [james_words, john_words, john_1_words]
    three_word_bank_titles = ["James", "John", "1st John"]

    six_word_banks = [james_words, john_words, john_1_words, john_2_words, john_3_words, revelation_words]
    six_word_bank_titles = ["James", "John", "1st John", "2nd John", "3rd John", "Revelation"]

    # printing the size of each book.
    # James 1764, John 15,930, Johns=2185,249,218 Rev=9960
    # for k in range(len(six_word_banks)):
    #     print(f"{six_word_bank_titles[k]} - len = {len(six_word_banks[k])}")

    word_banks = six_word_banks
    word_bank_titles = six_word_bank_titles

    word_searches = load_search_options()

    # Run most recent addtion to the word_searches.
    auto_selection = AUTO_SELECTION
    if USE_MOST_RECENT_SEARCH:
        auto_selection = len(word_searches) - 1  # sometimes I know what I want in advance (0 based index number)

    while True:
        if auto_selection is None:
            for k in range(len(word_searches)):
                print(f"{k + 1}. {word_searches[k].title}")
            selection = input("Select an option: ")
            if selection == "":
                print("Goodbye")
                break
            if selection.isnumeric():
                selection = int(selection) - 1  # Menu for humans is 1 based.
        else:
            selection = auto_selection
            print("Running auto selection", auto_selection)

        if selection < len(word_searches):
            run_word_search(word_searches[selection], word_banks, word_bank_titles, greek_dictionary_map)
        else:
            print("Invalid selection")

        if RUN_ONCE or auto_selection is not None:
            break  # Just do 1 run
        print("-----------------------------")


def load_search_options():
    word_searches = []
    teleios_options = WordSearchOptions(title="τέλειος - Perfect, mature, complete, whole",
                                        string_matches=["τέλ", "τελ", "τετελ", "τετέλ"],
                                        strong_numbers=["g5046", "g5055", "g5056", "g658", "g5048"])
    word_searches.append(teleios_options)

    adelphos_options = WordSearchOptions(title="ἀδελφὸς - Brothers or sisters",
                                        string_matches=["ἀδελφ", "αδελφ"],
                                        strong_numbers=["g79", "g80"])
    word_searches.append(adelphos_options)

    # Interesting in James only
    # tongue_options = WordSearchOptions(title="γλῶσσαν - The tongue, language",
    #                                     string_matches=["γλῶσσ"],
    #                                     strong_numbers=["g1100"])
    # word_searches.append(tongue_options)

    logos_options = WordSearchOptions(title="λόγῳ - Word",
                                        string_matches=["λόγ", "λογ", "λόγου", "λόγῳ"],
                                        strong_numbers=["g3056"])
    word_searches.append(logos_options)

    law_options = WordSearchOptions(title="νομος - Law",
                                        string_matches=["νομ", "νομο", "νόμο", "νόμ", "νόμό", "νομό"],
                                        strong_numbers=["g3551"])
    word_searches.append(law_options)

    # Interesting in James only
    # whole_options = WordSearchOptions(title="ολος - whole",
    #                                     string_matches=["ὁλό", "ὅλο"],
    #                                     strong_numbers=["g3648", "g3650"])
    # word_searches.append(whole_options)

    # Interesting in James only
    # all_options = WordSearchOptions(title="all",
    #                                     string_matches=["πᾶς", "πάσ", "πάν" ],
    #                                     strong_numbers=["g3956"])
    # word_searches.append(all_options)

    # More than 70
    jews_options = WordSearchOptions(title="Ἰουδαί - Jews",
                                        string_matches=["Ἰουδα".lower()],
                                        strong_numbers=["g2453"])
    word_searches.append(jews_options)

    # Only interesting in James
    ginosko_options = WordSearchOptions(title="γινώσκοντες - Knowing / experiencing",
                                        string_matches=["γινωσκω", "γινωσκέτω", "γιν", "γνῶναι"],
                                        strong_numbers=["g1097"])
    word_searches.append(ginosko_options)

    # Only interesting in John (10 in Rev)
    hour_options = WordSearchOptions(title="ὥρα - Hour ",
                                        string_matches=["ὥρα"],
                                        strong_numbers=["g5610"])
    word_searches.append(hour_options)

    day_options = WordSearchOptions(title="ἡμέρα and ἐπαύριον - Day and Next day",
                                        string_matches=["ἡμέρα", "ἐπαύριον"],
                                        strong_numbers=["g2250", "g1887", "g1476", "g839", "g2250"])
    word_searches.append(day_options)

    beginning_options = WordSearchOptions(title="ἀρχῇ - Beginning",
                                        string_matches=["ἀρχὴ", "ἀρχῆ"],
                                        strong_numbers=["g746", "g0756"])
    word_searches.append(beginning_options)



    god_options = WordSearchOptions(title="θεός - God",
                                        string_matches=["θεός"],
                                        strong_numbers=["g2316"])
    word_searches.append(god_options)



    lord_options = WordSearchOptions(title="κύριος - Lord",
                                        string_matches=["κύριος"],
                                        strong_numbers=["g2962"])
    word_searches.append(lord_options)

    jesus_options = WordSearchOptions(title="Ἰησοῦ - Jesus",
                                 string_matches=["Ἰησοῦ"],
                                 strong_numbers=["g2424"])
    word_searches.append(jesus_options)

    christ_options = WordSearchOptions(title="Χριστός - Christ",
                                        string_matches=["Χριστός"],
                                        strong_numbers=["g5547", "g5548"])
    word_searches.append(christ_options)


    so_many_options = WordSearchOptions(title="τοσούτων - so many",
                                        string_matches=["τοσούτω"],
                                        strong_numbers=["g5118"])
    word_searches.append(so_many_options)

    through_options = WordSearchOptions(title="through - δια",
                                        string_matches=["δια"],
                                        strong_numbers=["g1223"])
    word_searches.append(through_options)


    witness_options = WordSearchOptions(title="μαρτυρια - Witness",
                                        string_matches=["μαρ", "μαρτυ", "ἐμαρτ", "μεμαρτ"],
                                        strong_numbers=["g3140", "g3141"])
    word_searches.append(witness_options)

    come_options = WordSearchOptions(title="ερχομα - come",
                                        string_matches=["ερχ"],
                                        strong_numbers=["g2064"])
    word_searches.append(come_options)

    sent_options = WordSearchOptions(title="αποστελλω [apostello] sent and πεθπω sent- 1:6, 1:19, 1:24",
                                        string_matches=["αποσ", "πεθπω", "διδωμι"],
                                        strong_numbers=["g649", "g3992", "g1325"])
    word_searches.append(sent_options)

    sign_options = WordSearchOptions(title="σημεῖον - sign, mark, that which distinguishes(miracle)",
                                        string_matches=["σημε"],
                                        strong_numbers=["g4592"])
    word_searches.append(sign_options)

    amen_options = WordSearchOptions(title="Ἀμὴν ἀμὴν - Amen, amen Verily Verily",
                                        string_matches=["Ἀμὴν ἀμὴν"],
                                        strong_numbers=["g281"])
    word_searches.append(amen_options)

    desired_wanted_purposed_options = WordSearchOptions(title="θέλω desired wanted purposed",
                                        string_matches=["θέλω"],
                                        strong_numbers=["g2309"])
    word_searches.append(desired_wanted_purposed_options)

    made_options = WordSearchOptions(title="γινομαι - ginomai made",
                                        string_matches=["γέγο", "ἐγέ", "γενέ", "Ἐγέ", "γεγ"],
                                        strong_numbers=["g1096", "g1080"])
    made_options.starts_with_matches_only = False
    word_searches.append(made_options)

    born_options = WordSearchOptions(title="γεννάω - gennao born",
                                        string_matches=["γενν", "ἐγεννή"],
                                        strong_numbers=["g1080"])
    word_searches.append(born_options)

    begotten_options = WordSearchOptions(title="μονογενής - monogenes one and only begotten",
                                        string_matches=["μονογεν"],
                                        strong_numbers=["g3439"])
    word_searches.append(begotten_options)

    # 1. μονογενοῦς - of the only begotten (1:14.16) g3439 T1.1
    # 2. μονογενὴς - the only begotten (1:18.5) g3439 T1.1
    # 3. μονογενῆ - only begotten (3:16.12) g3439 T2.0
    # 4. μονογενοῦς - of the only begotten (3:18.19) g3439 T2.0

    begotten_and_others_options = WordSearchOptions(title="μονογενής - monogenes and others",
                                        string_matches=["γεννή", "γενοῦ", "γενὴ", "γενῆ", "γενοῦ"],
                                        strong_numbers=["g3439", "g3439", "g1080", "g4773"])

    begotten_and_others_options.starts_with_matches_only = False
    word_searches.append(begotten_and_others_options)

    wind_spirit_options = WordSearchOptions(title="πνεῦμα - pneuma wind spirit Spirit",
                                        string_matches=["πνεῦμα"],
                                        strong_numbers=["g4151"])
    word_searches.append(wind_spirit_options)


    water_options = WordSearchOptions(title="ὕδατος - water",
                                        string_matches=["ὕδατ", "νερο", "νεπό"],
                                        strong_numbers=["g5204", "g5201", "g5202", "g5203", "g504"])
    word_searches.append(water_options)


    believes_options = WordSearchOptions(title="πιστεύων - beleives",
                                        string_matches=["πιστεύων"],
                                        strong_numbers=["g4100"])
    word_searches.append(believes_options)

    anothen_options = WordSearchOptions(title="ἄνωθεν - anothen above",
                                        string_matches=["ἄνωθ"],
                                        strong_numbers=["g509"])
    word_searches.append(anothen_options)


    love_agape_options = WordSearchOptions(title="ἀγαπάω - to love",
                                        string_matches=["ἀγαπ"],
                                        strong_numbers=["g25", "g5368"])
    word_searches.append(love_agape_options)


    anthropos_options = WordSearchOptions(title="ανθρωπος - anthropos man",
                                        string_matches=["ἄανθρωπ"],
                                        strong_numbers=["g444"])
    word_searches.append(anthropos_options)

    men_options = WordSearchOptions(title="ανθρωπος - anthropos man and aner man",
                                        string_matches=["ἄανθρωπ"],
                                        strong_numbers=["g444", "g435", "g3700"])
    word_searches.append(men_options)

    lifted_up_options = WordSearchOptions(title="ὐψόω hupsoo - lifted_up",
                                        string_matches=["ὐψόω"],
                                        strong_numbers=["g5312"])
    word_searches.append(lifted_up_options)

    father_options = WordSearchOptions(title="πατήρ - Father, father",
                                        string_matches=["πατ"],
                                        strong_numbers=["g3962"])
    word_searches.append(father_options)

    seek_options = WordSearchOptions(title="ζητέω - seeks",
                                        string_matches=["ζητέ"],
                                        strong_numbers=["g2212"])
    word_searches.append(seek_options)

    draw_options = WordSearchOptions(title="ἄντλημα ἀντλέω - draw",
                                        string_matches=["ἄντλημα"],
                                        strong_numbers=["g502", "g501"])
    word_searches.append(draw_options)

    hour_options = WordSearchOptions(title="ὤρα - Hour",
                                        string_matches=["ὤρα"],
                                        strong_numbers=["g5610"])
    word_searches.append(hour_options)

    reaps_options = WordSearchOptions(title="θερίζω - reaps",
                                        string_matches=["θερίζ"],
                                        strong_numbers=["g2325"])
    word_searches.append(reaps_options)

    sows_options = WordSearchOptions(title="σπείρω - sows",
                                        string_matches=["σπείρ"],
                                        strong_numbers=["g4687"])
    word_searches.append(sows_options)

    worship_options = WordSearchOptions(title="προσκυνέω – worship",
                                        string_matches=["προσκ"],
                                        strong_numbers=["g4352", "g4353"])
    word_searches.append(worship_options)


    mother_options = WordSearchOptions(title="προσκυνέω – mother",
                                        string_matches=["προσκ"],
                                        strong_numbers=["g4352", "g4353"])
    word_searches.append(mother_options)

    believe_options = WordSearchOptions(title=" πιστεύ – faith / believe / trust",
                                        string_matches=["πιστεύ"],
                                        strong_numbers=["g4100", "g4102"])
    word_searches.append(believe_options)

    rejoiced_options = WordSearchOptions(title="  – rejoice and be glad",
                                        string_matches=[""],
                                        strong_numbers=[""])
    word_searches.append(rejoiced_options)

    ch11_come_options = WordSearchOptions(title=" - Come (come and see)",
                                        string_matches=[""],
                                        strong_numbers=[""])
    word_searches.append(ch11_come_options)

    ch11_see_options = WordSearchOptions(title=" - See (come and see)",
                                          string_matches=[""],
                                          strong_numbers=[""])
    word_searches.append(ch11_see_options)

    ch11_remove = WordSearchOptions(title=" - Remove (raise off)",
                                          string_matches=[""],
                                          strong_numbers=[""])
    word_searches.append(ch11_remove)

    glory_searches = WordSearchOptions(title="δοξάζω - Glory, glorify",
                                          string_matches=["δοξάζ"],
                                          strong_numbers=["g1391", "g1392"])
    word_searches.append(glory_searches)

    # Interesting words to consider:
    #  water, testimony, witness, grace, grace and truth, name


    # _options = WordSearchOptions(title="",
    #                                     string_matches=[""],
    #                                     strong_numbers=[""])
    # word_searches.append(_options)


    # _options = WordSearchOptions(title="",
    #                                     string_matches=[""],
    #                                     strong_numbers=[""])
    # word_searches.append(_options)

    # Other words with progess, left over from James.

    # print("5. ὑπομονὴ - Perserverance, endurance")
    # print_matches(all_words, ["ὑπομ", "υπομ"])
    # find_strongs(all_words, ["g5278", "g5281" ], print_only=True)  # Perseverance
    # find_strongs(all_words, ["g3985"], print_only=True)  # Perseverance

    # print("6. πειρασμοῖς - Trials")
    #   print_matches(all_words, ["πειρασμοῖς", "πειρασ"])
    # find_strongs(all_words, ["g3986"], print_only=True)  # Trials

    # print("7. πειραζόμενος - Temptations")
    #   print_matches(all_words, ["πειραζόμενος", "πειραζόμ", "πειράζομαι", "πειράζει", "ἀπείραστός"])
    # find_strongs(all_words, ["g3985"], print_only=True)  # Temptations (1)
    # find_strongs(all_words, ["g551"], print_only=True)  # Temptations (2)

    # Knowing eido
    # find_strongs(all_words, ["g1492"], print_only=True)  # Knowing eido
    #   print_matches(all_words, ["εἰδ", "ἔστω", "οἴδ"])

    # print("9. λειπόμενοι - Lacking")
    #   print_matches(all_words, ["λειπ", "λέιπ", "λείπ", "λέίπ"])
    #   print_matches(all_words, ["λει", "λέι", "λεί", "λέί"])

    # print("10. πόλεμοι καὶ μάχαι - Wars and battles")
    #   print_matches(all_words, ["πόλεμοι", "μάχαι", "μάχεσθε", "πολεμεῖτε"])

    # print("11. σοφίας - Wisdom")
    #   print_matches(all_words, ["σοφίας", "σοφ"])

    # print("12. ἁμαρτίαν - Sin")
    #   print_matches(all_words, ["ἁμαρτίαν", "αμαρ"])

    # print("13. πλούσιος - Rich")
    #   print_matches(all_words, ["πλούσιος", "πλού", "πλου"])

    # print("14. ἔργων - Works, deeds")
    #   print_matches(all_words, ["εργ", "ἔργων", "ἔργω", "ἔργ"])

    # print("15. ταπεινὸς - Humble / low position")
    #   print_matches(all_words, ["πραντης", "ταπει", "ταπει", "ταπεινὸς"])

    # print("16. πραΰτητι - Humble / gentleness / meekness")
    #   print_matches(all_words, ["πραΰτητι", "πρα"])

    # print("19. κρινω - Judging")
    #   print_matches(all_words, ["κρισις", "κρινω", "κρίσεως", "κρίσις", "κρίσ", "κρίσ", "κρί", "κρι"])

    # print("20. αὐτοῦ - His")
    #   print_matches(all_words, ["αὐτοῦ", "αὐτο", "αυτο"])

    return word_searches


def run_word_search(search_options, concordance_words, concordance_titles, dictionary_map):
    print()
    print("--------------------------------------------------------------------")
    print(f"Start: {search_options.title}")
    print("--------------------------------------------------------------------")
    for strong_code in search_options.strong_numbers:
        print(dictionary_map[strong_code])
    print("--------------------------------------------------------------------")
    print()
    if search_options.starts_with_matches_only:
        print("   ----------------- Results for Starts with string matches ----------------- ")
    else:
        print("  ----------------- Results for Contains string matches ----------------- ")
    print("  ", search_options.string_matches)
    for k in range(len(concordance_words)):
        print()
        print(f"    ----------------- {concordance_titles[k]} -----------------")
        find_matches(concordance_words[k], search_options.string_matches, starts_with_matches_only=search_options.starts_with_matches_only)
    print()
    print("   ----------------- Strong's Number search results ----------------- ")
    print("  ", search_options.strong_numbers)
    for k in range(len(concordance_words)):
        print()
        print(f"    ----------------- {concordance_titles[k]} -----------------")
        find_strongs(concordance_words[k], search_options.strong_numbers, print_only=True)
    print()
    print("--------------------------------------------------------------------")
    print(f"End: {search_options.title}")
    print("--------------------------------------------------------------------")
    print()


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


def load_dictionary(dictionary_filename):
    dictionary_json_file = open(f"../data/dictionaries/{dictionary_filename}")

    words_maps_list = json.load(dictionary_json_file)
    dictionary_map = {}

    for word_map in words_maps_list:
        strong_word = StrongWord(word_map)
        dictionary_map[strong_word.number] = strong_word

    dictionary_json_file.close()
    return dictionary_map


def load_greek_concordance(concordance_filename):
    greek_concordance_json_file = open(f"../data/greek_concordances/{concordance_filename}")

    verse_maps = json.load(greek_concordance_json_file)
    greek_words = []

    for single_verse in verse_maps:
        current_chapter = int(single_verse["id"][2:5])
        current_verse = int(single_verse["id"][5:])
        current_fisher_section = get_fisher_section(concordance_filename, current_chapter, current_verse)
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
            if strongs_number == word.strongs_number and word.verse_index != prior_verse_index:
                found = True
                prior_verse_index = word.verse_index
        if found:
            if print_only:
                print(f"    {hits}. {word}")
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
                if word.greek_word.lower().startswith(match.lower()):
                    found = True
            else:
                if match.lower() in word.greek_word.lower():
                    found = True
        if found:
            if print_only:
                print(f"    {hits}. {word}")
                hits += 1
            else:
                greek_word_matches.append(word)
    return greek_word_matches


def get_fisher_section(concordance_filename, chapter, verse):
    if concordance_filename.startswith("james"):
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
    elif concordance_filename.startswith("john"):
        if chapter == 1:
            if verse <= 19:
                return 1.1
            else:
                return 2.3
        else:
            return 2.0
    else:
        return 0


if __name__ == "__main__":
    main()
