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
