# Data Files

Getting high quality data files are one of the hardest parts of making useful biblical concordance scripts.  Finding them is difficult and having proper licenses for them is even more difficult. 

Here is where I found some of the files I've been using.

---

The concordance folder, the _concordance.json files, are based on the SBLGNT translation and come from this github repo:
[https://github.com/tahmmee/interlinear_bibledata](https://github.com/tahmmee/interlinear_bibledata)

from their README.md

    Interlinear OT and NT with strongs numbers
    All the text here is public domain
    Original concordance data is from here: https://github.com/camertron/cskit-strongs-rb
    However the verse structures are unordered. So This projects re-orders this data by using original language concordance as found here: https://github.com/bibleforge/BibleForgeDB/blob/master/bible_original.sql.gz

 * The concordance folder, the _concordance.json files, are in the [interlinear/bible.tar.gz](https://github.com/tahmmee/interlinear_bibledata/tree/master/interlinear) compressed file.
 * The dictionary folder, greek.json and hebrew.json files, are from their [lexicon](https://github.com/tahmmee/interlinear_bibledata/tree/master/lexicon) folder.

---

The greek text folder, _greek.txt files, are based on the SBLGNT translation and come from this github repo:
[https://github.com/LogosBible/SBLGNT](https://github.com/LogosBible/SBLGNT)
specifically the 
[/data/sblgnt/text](https://github.com/LogosBible/SBLGNT/tree/master/data/sblgnt/text) folder.

from their README.md

    The SBL Greek New Testament (SBLGNT), is a new, critically edited edition of the Greek New Testament. It is freely available in electronic form, to be useful to students, teachers, translators, and scholars in a wide variety of settings and contexts.

    For more information, see About and the SBLGNT website.

---

The niv text folder, _niv.json files, I don't really use.  I prefer to typically just go to [biblegateway.com](https://www.biblegateway.com/) and look things up.  The _niv.json files were generated files that are the output or running the getting_bible_text.py file.  You can see that file for specifics about how those json files were generated and formatted.
