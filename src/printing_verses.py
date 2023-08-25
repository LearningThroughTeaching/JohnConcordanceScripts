import json


def main():
    book = "john"
    print(f"--- Printing {book.title()} NIV2011 ---")
    all_chapters = load_niv(f"../data/niv_text/{book}_niv.json")
    # for chapter in all_chapters:
    #     print_chapter(book, chapter)

    print_chapter(book, all_chapters[0])


def print_chapter(book, chapter_json):
    chapter = chapter_json['chapter']
    print()
    print(f"{book.title()} Chapter {chapter}.")
    print()
    for verse in chapter_json["verses"]:
        print(f" {verse['verse']} ", end="")
        print(verse["text"], end="")
    print()


def load_niv(json_niv_filename):
    json_file = open(json_niv_filename)
    all_chapters = json.load(json_file)
    json_file.close()
    return all_chapters


if __name__ == "__main__":
    main()
