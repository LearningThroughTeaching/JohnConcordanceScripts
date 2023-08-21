from PyDictionary import PyDictionary
dictionary=PyDictionary()
# print(dictionary.translateTo("en"))
#"τέλειοι", "τέλειον", "τέλειον", "τέλειον", "τέλειος", "τέλος", "τελεῖτε", "ἀποτελεσθεῖσα", "ἐτελειώθη"
print(dictionary.translate("τέλειον", "en"))
print(dictionary.translate("τέλειος", "en"))

# perfect_dict = PyDictionary("τέλειοι", "τέλειον", "τέλειον", "τέλειον", "τέλειος", "τέλος", "τελεῖτε", "ἀποτελεσθεῖσα", "ἐτελειώθη")
# print(perfect_dict.translateTo("en"))
