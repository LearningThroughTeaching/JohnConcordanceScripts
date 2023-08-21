import unicodedata as ud
import unidecode

s="Ο πάνω όροφος"
s="γινωσκετω ὁτι ὁ ἐπιστρεψας ἁμαρτωλὸν ἐκ πλανης ὁδοῦ αὐτοῦ σωσει ψυχὴν ⸀αὐτοῦ ἐκ θανατου καὶ καλυψει πλῆθος ἁμαρτιῶν."

diacritics_table = {ord('\N{COMBINING ACUTE ACCENT}'):None}

print(s)
print(ud.normalize("NFKD",s).lower().translate(diacritics_table))

# display original string
print('\nOriginal String:', s)

# remove ascents
outputString = unidecode.unidecode(s)

# display new string
print('\nNew String:', outputString)