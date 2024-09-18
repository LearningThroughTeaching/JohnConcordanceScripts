class WordSearchOptions:

    def __init__(self, title, string_matches, strong_numbers):
        self.title = title
        self.string_matches = string_matches
        self.strong_numbers = strong_numbers
        self.starts_with_matches_only = True

    def __repr__(self):
        return self.title