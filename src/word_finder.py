import unidecode
TRANSLITERATE = False


def main():
  greek_text_file = open("../data/greek_text/john_greek.txt", "r")
  words = []
  for line in greek_text_file:
    if TRANSLITERATE:
      line = unidecode.unidecode(line)
    words += line.split()
  greek_text_file.close()

  current_verse = "1:1"
  all_words = []
  verse_words = []
  for word in words:
    if "John" in word:
      continue
    if ":" in word:  # Add the prior verse only on next verse (not a great system)
      current_verse = word
      all_words += verse_words
      verse_words.clear()
      continue
    next_word = word.strip().lower()
    for special_char in "⸂⸃·,.⸀;":  # DIY regex
      next_word = next_word.replace(special_char, "")
    if len(next_word) > 0:
      verse_words.append(next_word + " " + current_verse)
  all_words += verse_words  # Verses are only added when the next verse is seen, so add last verse.

  RUN_ONCE = False
  AUTO_SELECTION = None
  # AUTO_SELECTION = "1"  # sometimes I know what I want in advance.
  print("0. Run the 'potential chaining words' script")
  print("1. τέλειος - Perfect, mature, complete, whole")
  print("2. ἀδελφὸς - Brothers or sisters")
  print("3. γλῶσσαν - The tongue, language")
  print("4. ολος - whole")
  print("5. ὑπομονὴ - Perserverance, endurance")
  print("6. πειρασμοῖς - Trials")
  print("7. πειραζόμενος - Temptations")
  print("8. γινώσκοντες - Knowing / experiencing")
  print("8b. γινώσκοντες - Knowing / experiencing")
  print("9. λειπόμενοι - Lacking")
  print("10. πόλεμοι καὶ μάχαι - Wars and battles")
  print("11. σοφίας - Wisdom")
  print("12. ἁμαρτίαν - Sin")
  print("13. πλούσιος - Rich")
  print("14. ἔργων - Works, deeds")
  print("15. ταπεινὸς - Humble / low position")
  print("16. πραΰτητι - Humble / gentleness / meekness")
  print("17. λόγῳ - Word")
  print("18. νομος - Law")
  print("19. κρινω - Judging")
  print("20. αὐτοῦ - His")
  while True:
    if AUTO_SELECTION is None:
      selection = input("Select an option or type a word: ")
    else:
      selection = AUTO_SELECTION
      print("Running auto selection", AUTO_SELECTION)
    if selection == "":
      print("Goodbye")
      break
    elif selection == "0":
      potential_chaining_words(all_words)
    elif selection == "1":
      print_matches(all_words, ["τέλ", "τελ"])
    elif selection == "2":
      print_matches(all_words, ["ἀδελφ", "αδελφ"])
    elif selection == "3":
      print_matches(all_words, ["γλῶσσ"])
    elif selection == "4":
      print_matches(all_words, ["ὁλό", "ὅλο"])
    elif selection == "5":
      print_matches(all_words, ["ὑπομ", "υπομ"])
    elif selection == "6":
      print_matches(all_words, ["πειρασμοῖς", "πειρασ"])
    elif selection == "7":
      print_matches(all_words, ["πειραζόμενος", "πειραζόμ", "πειράζομαι", "πειράζει", "ἀπείραστός"])
    elif selection == "8":
      print_matches(all_words, ["γινωσκω", "γινωσκέτω", "γιν", "γνῶναι"])
    elif selection == "8b":
      print_matches(all_words, ["εἰδ", "ἔστω", "οἴδ"])
    elif selection == "9":
      print_matches(all_words, ["λειπ", "λέιπ", "λείπ", "λέίπ"])
      print_matches(all_words, ["λει", "λέι", "λεί", "λέί"])
    elif selection == "10":
      print_matches(all_words, ["πόλεμοι", "μάχαι", "μάχεσθε", "πολεμεῖτε"])
    elif selection == "11":
      print_matches(all_words, ["σοφίας", "σοφ"])
    elif selection == "12":
      print_matches(all_words, ["ἁμαρτίαν", "αμαρ"])
    elif selection == "13":
      print_matches(all_words, ["πλούσιος", "πλού", "πλου"])
    elif selection == "14":
      print_matches(all_words, ["εργ", "ἔργων", "ἔργω", "ἔργ"])
    elif selection == "15":
      print_matches(all_words, ["πραντης", "ταπει", "ταπει", "ταπεινὸς"])
    elif selection == "16":
      print_matches(all_words, ["πραΰτητι", "πρα"])
    elif selection == "17":
      print_matches(all_words, ["λόγου", "λόγῳ", "λόγον"])
    elif selection == "18":
      print_matches(all_words, ["νομος", "νομο", "νόμο", "νόμό", "νομό"])
    elif selection == "19":
      print_matches(all_words, ["κρισις", "κρινω", "κρίσεως", "κρίσις", "κρίσ", "κρίσ", "κρί", "κρι"])
    elif selection == "20":
      print_matches(all_words, ["αὐτοῦ", "αὐτο", "αυτο"])

    else:
      print_matches(all_words, [selection])
    if RUN_ONCE or AUTO_SELECTION is not None:
      break
    print("-----------------------------")


def print_matches(all_words, matches):
  hits = 1
  for word in all_words:
    found = False
    for match in matches:
      if match in word:
        found = True
    if found:
        print(f"{hits}. {word}")
        hits += 1


def get_verse_index(word):
  word_and_verse = word.split()
  chapter_and_verse = word_and_verse[1].split(":")
  return int(chapter_and_verse[0]) * 100 + int(chapter_and_verse[1]), word_and_verse[0]


def potential_chaining_words(all_words):

  # Words used twice in succession - chaining words
  potential_chaining_words = []
  sorted_all_words = sorted(all_words)
  prior_verse = 0
  prior_word = ""
  for word in sorted_all_words:
    current_verse, greek_word = get_verse_index(word)
    if abs(current_verse - prior_verse) <= 1 and len(greek_word) > 4:
      potential_chaining_words.append(prior_word + "(" + str(prior_verse//100) + ":" + str(prior_verse % 100) + ")" + "-->" + word)
    prior_verse = current_verse
    prior_word = greek_word

  potential_chaining_words.sort(key=lambda word: get_verse_index(word))
  for word in potential_chaining_words:
    print(word)

main()
