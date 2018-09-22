# romaji switch
# set to True if you want romaji in your cards, False otherwise
INCLUDE_ROMAJI = True

# if set to true, user won't be prompted for meanings choices with each and every words
LAZY_MEANINGS = False

# a limit to number of meanings that should be saved in your flashcards (provided LAZY_MEANINGS is set to True)
# set to a positive integer to limit a number of meanings that will be saved, or 0 for no limit
MEANING_LIMIT = 2

# path to the file storing scrapped words, relative to your user (~) directory
# you'll be using that file with anki
CSV_FILE_PATH = "Uczelnia/Projekty/DictionaryScraper/dictscraper/resources/csv_file.txt"

# if set to true, when a connection error occurs, requested words will be stored in a separate file
QUEUE_IF_CONNECTION_ERROR = True
