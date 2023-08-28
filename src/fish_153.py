import unidecode

# Fish
ichthys = unidecode.unidecode("ἰχθύς")
print(ichthys)
# ikhthus
# yod (10) + tsadi? (90) + tav (400) <-- too big

lord = unidecode.unidecode("κύριος")
print(lord)
# kurios
# kaf (20) ? resh (200) <-- too big

jesus = unidecode.unidecode("Ἰησοῦ")
print(jesus)
# yod (10) maybe chet (8) samech (60) vav (6) alef (1) vav (6)
print(10+8+60+6+1+6) # 91

christ = unidecode.unidecode("Χριστός")
print(christ)
# has a resh, too big, just stop

# Kepha
# kaf (20) + chet (8) + pe (80) + alef (1) = 109
# Κηφᾶς
# kaf (20) + chet (8) + pe (80) + alef (1) + samech (60) = 169

# It's probably really close to the 153.
#ἀνέβη ⸀οὖν Σίμων Πέτρος καὶ εἵλκυσεν τὸ δίκτυον ⸂εἰς τὴν γῆν⸃ μεστὸν ἰχθύων μεγάλων ἑκατὸν πεντήκοντα τριῶν· καὶ τοσούτων ὄντων οὐκ ἐσχίσθη τὸ δίκτυον.

# large fish
# μεγάλων  ἰχθύων
large = unidecode.unidecode("μεγάλων")
print(large)

# megalon  --> megalOn
# mem (40) + chet (8) + gimel (3) + alef (1) + lamed (30) + vav (6) + nun (50)
megalon_value = 40 + 8 + 3 + 1 + 30 + 6 + 50
print(megalon_value) # 138

# μεστὸν - distended (stretched) as in the net
stretched_net = unidecode.unidecode("μεστὸν")
print(stretched_net)
# meston
# mem (40) + chet (8) + samech (60) + tet (9) + vav (6) + nun (50)
meston_value = 40 + 8 + 60 + 9 + 6 + 50
print(meston_value) # 173

# Mary
# η Μαγδαληνή
# 8 + 40 + 1 + 3 + 4 + 1 + 30 + 8 + 50 + 8 = 153
# Note: eta they do 8 (chet) consistently
# chet + Mem (40) + alef (1) + gimel (3) + delet (4) + alef (1) + lamed (30) + chet (8) + nun (50) + chet (8)
# Neat, but not related at all.

# All the words here...
# τὸ δίκτυον (the net)
# ⸂εἰς (on) τὴν (the) γῆν⸃ (land) μεστὸν (stretched) ἰχθύων (fish) μεγάλων (large)
# ἑκατὸν (100) πεντήκοντα (50) τριῶν (3) --> 153
# καὶ (and) τοσούτων (so many) ὄντων (being) οὐκ (not) ἐσχίσθη (broken)
# τὸ δίκτυον (the net).

the_net = unidecode.unidecode("τὸ δίκτυον")
print(the_net)
# to diktuon
# tet (9) + vav (6) + delet (4) + iota-yod (10) + kaf (20) + tet (9) + vav (6) + alef (1) + vav (6) + nun (50)
the_net_value = 9 + 6 + 4 + 10 + 20 + 9 + 6 + 1 + 6 + 50
print(the_net_value) # 121

# καὶ (and) τοσούτων (so many) ὄντων (being) οὐκ (not) ἐσχίσθη (broken)
# https://en.wikipedia.org/wiki/153_(number)#In_the_Bible

# οὐκ (not) ἐσχίσθη (broken)
not_broken = unidecode.unidecode("οὐκ ἐσχίσθη")
print(not_broken)
# ouk eskhisthe (or eschishthE)
# vav (6) + 0 + kaf (20) + samech (60) + chet (8 or 20) + yod (10) + samech (60) + tav (400) + chet (8)
not_broken_value = 6 + 20 + 60 + 8 + 10 + 60 + 400 + 8
print(not_broken_value) #572

# τοσούτων (so many)
quantity_so_great = unidecode.unidecode("τοσούτων")
print(quantity_so_great)
# tosouton
# tet (9) + vav (6) + samech (60) + vav (6) + Note, Alef is needed here! + vav (6) + tet (9) + vav (6) + nun (50)
so_many_value = 9 + 6 + 60 + 6 + 1 + 6 + 9 + 6 + 50
print(so_many_value) #153

# Note, at first I got 152 not 153...

# 153 = τοσούτων i.e. such a great number (152) + 1 more
# This is the best I've got for now, time for real work.

# How I got to 153:

# https://charlesloder.github.io/greekTransliteration/
# τοσούτων --> tosoutōn

# https://hebrewtransliteration.app
# this is where I noticed the need for an alef between the ou to break up the double vav issue.
# טוֹסוֹוּטון
# would be ṭôsōwûṭwn, however by adding an alef between the ou it works to be toso`utwn
# טוֹסוֹאוּטון
# results in toso`utwn
# Bingo!
# Tet + vav(as in o) + samech + vav(as in o) + alef (to separate the double vav) + vav(as in u) + tet + vav (as in omega) + final nun
# 9 + 6 + 60 + 6 + 1 + 6 + 9 + 6 + 50
print(9 + 6 + 60 + 6 + 1 + 6 + 9 + 6 + 50)  #153

# John was such a math dork! (as am I)
