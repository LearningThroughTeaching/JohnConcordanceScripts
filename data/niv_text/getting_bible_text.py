# This was just a little script I put together to quickly grab the
# text of the NIV2011 bible.  Honestly I could've probably copied
# the text from somewhere online, but this let me put the NIV2011
# into a .json file in a format of my choosing.  For example the start of
#
# john_niv.json
#
# [
#     {
#         "chapter": 1,
#         "verses": [
#             {
#                 "pk": 3316913,
#                 "verse": 1,
#                 "text": "In the beginning was the Word, and the Word was with God, and the Word was God."
#             },

# There is no need to run this file again.  I ran it for:
# john, james, john1, john2, john3
# and now those files are made.  The script is handy if you want more I guess.

# Learning the Bolls Life API.
# https://bolls.life/get-books/NIV2011/
#
# [{"bookid": 1, "name": "Genesis", "chronorder": 1, "chapters": 50},
#  {"bookid": 2, "name": "Exodus", "chronorder": 3, "chapters": 40},
#  {"bookid": 3, "name": "Leviticus", "chronorder": 4, "chapters": 27},
#  {"bookid": 4, "name": "Numbers", "chronorder": 5, "chapters": 36},
#  {"bookid": 5, "name": "Deuteronomy", "chronorder": 6, "chapters": 34},
#  {"bookid": 6, "name": "Joshua", "chronorder": 7, "chapters": 24},
#  {"bookid": 7, "name": "Judges", "chronorder": 8, "chapters": 21},
#  {"bookid": 8, "name": "Ruth", "chronorder": 9, "chapters": 4},
#  {"bookid": 9, "name": "1 Samuel", "chronorder": 10, "chapters": 31},
#  {"bookid": 10, "name": "2 Samuel", "chronorder": 11, "chapters": 24},
#  {"bookid": 11, "name": "1 Kings", "chronorder": 15, "chapters": 22},
#  {"bookid": 12, "name": "2 Kings", "chronorder": 28, "chapters": 25},
#  {"bookid": 13, "name": "1 Chronicles", "chronorder": 12, "chapters": 29},
#  {"bookid": 14, "name": "2 Chronicles", "chronorder": 16, "chapters": 36},
#  {"bookid": 15, "name": "Ezra", "chronorder": 37, "chapters": 10},
#  {"bookid": 16, "name": "Nehemiah", "chronorder": 38, "chapters": 13},
#  {"bookid": 17, "name": "Esther", "chronorder": 36, "chapters": 10},
#  {"bookid": 18, "name": "Job", "chronorder": 2, "chapters": 42},
#  {"bookid": 19, "name": "Psalm", "chronorder": 13, "chapters": 150},
#  {"bookid": 20, "name": "Proverbs", "chronorder": 17, "chapters": 31},
#  {"bookid": 21, "name": "Ecclesiastes", "chronorder": 18, "chapters": 12},
#  {"bookid": 22, "name": "Song of Songs", "chronorder": 14, "chapters": 8},
#  {"bookid": 23, "name": "Isaiah", "chronorder": 25, "chapters": 66},
#  {"bookid": 24, "name": "Jeremiah", "chronorder": 29, "chapters": 52},
#  {"bookid": 25, "name": "Lamentations", "chronorder": 30, "chapters": 5},
#  {"bookid": 26, "name": "Ezekiel", "chronorder": 32, "chapters": 48},
#  {"bookid": 27, "name": "Daniel", "chronorder": 33, "chapters": 12},
#  {"bookid": 28, "name": "Hosea", "chronorder": 23, "chapters": 14},
#  {"bookid": 29, "name": "Joel", "chronorder": 20, "chapters": 3},
#  {"bookid": 30, "name": "Amos", "chronorder": 21, "chapters": 9},
#  {"bookid": 31, "name": "Obadiah", "chronorder": 31, "chapters": 1},
#  {"bookid": 32, "name": "Jonah", "chronorder": 19, "chapters": 4},
#  {"bookid": 33, "name": "Micah", "chronorder": 22, "chapters": 7},
#  {"bookid": 34, "name": "Nahum", "chronorder": 24, "chapters": 3},
#  {"bookid": 35, "name": "Habakkuk", "chronorder": 27, "chapters": 3},
#  {"bookid": 36, "name": "Zephaniah", "chronorder": 26, "chapters": 3},
#  {"bookid": 37, "name": "Haggai", "chronorder": 34, "chapters": 2},
#  {"bookid": 38, "name": "Zechariah", "chronorder": 35, "chapters": 14},
#  {"bookid": 39, "name": "Malachi", "chronorder": 39, "chapters": 4},
#  {"bookid": 40, "name": "Matthew", "chronorder": 40, "chapters": 28},
#  {"bookid": 41, "name": "Mark", "chronorder": 58, "chapters": 16},
#  {"bookid": 42, "name": "Luke", "chronorder": 52, "chapters": 24},
#  {"bookid": 43, "name": "John", "chronorder": 66, "chapters": 21},
#  {"bookid": 44, "name": "Acts", "chronorder": 54, "chapters": 28},
#  {"bookid": 45, "name": "Romans", "chronorder": 46, "chapters": 16},
#  {"bookid": 46, "name": "1 Corinthians", "chronorder": 44, "chapters": 16},
#  {"bookid": 47, "name": "2 Corinthians", "chronorder": 45, "chapters": 13},
#  {"bookid": 48, "name": "Galatians", "chronorder": 41, "chapters": 6},
#  {"bookid": 49, "name": "Ephesians", "chronorder": 47, "chapters": 6},
#  {"bookid": 50, "name": "Philippians", "chronorder": 49, "chapters": 4},
#  {"bookid": 51, "name": "Colossians", "chronorder": 50, "chapters": 4},
#  {"bookid": 52, "name": "1 Thessalonians", "chronorder": 42, "chapters": 5},
#  {"bookid": 53, "name": "2 Thessalonians", "chronorder": 43, "chapters": 3},
#  {"bookid": 54, "name": "1 Timothy", "chronorder": 55, "chapters": 6},
#  {"bookid": 55, "name": "2 Timothy", "chronorder": 59, "chapters": 4},
#  {"bookid": 56, "name": "Titus", "chronorder": 57, "chapters": 3},
#  {"bookid": 57, "name": "Philemon", "chronorder": 51, "chapters": 1},
#  {"bookid": 58, "name": "Hebrews", "chronorder": 53, "chapters": 13},
#  {"bookid": 59, "name": "James", "chronorder": 48, "chapters": 5},
#  {"bookid": 60, "name": "1 Peter", "chronorder": 56, "chapters": 5},
#  {"bookid": 61, "name": "2 Peter", "chronorder": 60, "chapters": 3},
#  {"bookid": 62, "name": "1 John", "chronorder": 61, "chapters": 5},
#  {"bookid": 63, "name": "2 John", "chronorder": 62, "chapters": 1},
#  {"bookid": 64, "name": "3 John", "chronorder": 63, "chapters": 1},
#  {"bookid": 65, "name": "Jude", "chronorder": 64, "chapters": 1},
#  {"bookid": 66, "name": "Revelation", "chronorder": 65, "chapters": 22}]

import requests
import json
import asyncio


async def get_chapter(ch, book=43, translation="NIV2011"):
    response_api = requests.get(f"https://bolls.life/get-text/{translation}/{book}/{ch}/")
    print(response_api.status_code)
    json_data = json.loads(response_api.text)
    return json_data


async def main(book_filename, book_number, num_chapters):
    entire_book = []
    for k in range(1, num_chapters + 1):
        print(f"Fetching {book_filename} chapter", k)
        verse_array = await get_chapter(k, book=book_number)
        chapter_dict = {
            "chapter": k,
            "verses": verse_array
        }
        entire_book.append(chapter_dict)

    print(f"Writing {book_filename} chapters to file.")
    json_object = json.dumps(entire_book, indent=4)
    with open(f"{book_filename}_niv.json", "w") as outfile:
        outfile.write(json_object)
    print("Done")

loop = asyncio.get_event_loop()

# To add a book use this format...
# loop.run_until_complete(main(book_filename, book_number, num_chapters):)


# Examples: History of prior jobs:

#  {"bookid": 40, "name": "Matthew", "chronorder": 40, "chapters": 28},
#  {"bookid": 41, "name": "Mark", "chronorder": 58, "chapters": 16},
#  {"bookid": 42, "name": "Luke", "chronorder": 52, "chapters": 24},
#  {"bookid": 43, "name": "John", "chronorder": 66, "chapters": 21},
#  {"bookid": 44, "name": "Acts", "chronorder": 54, "chapters": 28},

# loop.run_until_complete(main("matthew", 40, 28))
# loop.run_until_complete(main("mark", 41, 16))
# loop.run_until_complete(main("luke", 42, 24))
# # loop.run_until_complete(main("john", 43, 21))
# loop.run_until_complete(main("acts", 44, 28))

# For {"bookid": 43, "name": "John", "chapters": 21} I ran:
# loop.run_until_complete(main("john", 43, 21))

#  {"bookid": 59, "name": "James", "chapters": 5},
# loop.run_until_complete(main("james", 59, 5))

#  {"bookid": 62, "name": "1 John", "chapters": 5},
# loop.run_until_complete(main("1_john", 62, 5))

#  {"bookid": 63, "name": "2 John",  "chapters": 1},
# loop.run_until_complete(main("2_john", 63, 1))

#  {"bookid": 64, "name": "3 John", "chapters": 1},
# loop.run_until_complete(main("3_john", 64, 1))

loop.close()
print("Done with main")

