# Detect English module
# https://www.nostarch.com/crackingcodes (BSD Licensed)

# To use, type this code:
#   import detectEnglish
#   detectEnglish.isEnglish(someString) # returns True or False
# (There must be a "dictionary.txt" file in this directory with all English
# words in it, one word per line. You can download this from
# https://invpy.com/dictionary.txt)
letters = 'abcdefghijklmnñopqrstuvwxyz'
vocal_acent = 'áéíóú'
symbols = '1234567890 !?.'
alphabet = letters + letters.upper() + vocal_acent + vocal_acent.upper() + symbols + '\t\n'

def loadDictionary():
    #dictionaryFile = open('dictionary.txt')
    dictionaryFile = open('dictEsp.txt', "r", encoding='utf_8')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords

SPANISH_WORDS = loadDictionary()

def getEnglishCount(message):
    message = removeNonLetters(message)
    print("Mensaje: ", message)
    possibleWords = message.split()

    if not possibleWords:
        return 0.0 # No words at all, so return 0.0.
    else:
        matches = 0
        for word in possibleWords:
            if word in SPANISH_WORDS:
                matches += 1
        return int(matches) / len(possibleWords)


def removeNonLetters(message):
    lettersOnly = ""
    for caracter in message:
        if caracter in alphabet:
            lettersOnly += str(caracter)
    return lettersOnly


def isSpanish(message, wordPercentage=20, letterPercentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).

    wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPercentage
    if wordsMatch and lettersMatch == True:
        print("Language Spanish")
    else:
        print("Other Language")
