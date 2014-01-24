import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    abc = list(string.ascii_lowercase)    
    for lets in lettersGuessed: 
        if lets in abc:
            abc.pop(abc.index(lets))
    abc1 = ""
    for lets in abc:
        abc1 += str(lets)
    return str(abc1)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CoDE HERE...
    newstr = ""
    lettersGuessed = str(lettersGuessed)
    #print lettersGuessed.find("a")
    for letters in secretWord:
        if lettersGuessed.count(letters) == 0:
            newstr += "_ "
        else:
            #print lettersGuessed.count(letters)
            for it in range(lettersGuessed.count(letters)):
                newstr+= letters
    return newstr


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CoDE HERE...
    count = 0
    for ls in lettersGuessed:
        #print count
        #print ls
        if ls in secretWord:
            count+=1
    if count == len(secretWord):
        return True
    else:
        return False
        
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = ""
    letterlist = ""
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long"
    #print secretWord
    #print lettersGuessed
    #print getAvailableLetters(lettersGuessed)
    while guesses > 0:
        print "-----------"
        print "You have "+str(guesses)+ " guesses left"
        print "Available letters: "+str(getAvailableLetters(letterlist))
        lettersGuessed = raw_input("Please guess a letter: ")
        lettersGuessed = str(lettersGuessed).lower()
        #if lettersGuessed not in string.ascii_lowercase:
           # print "Opps that was an invalid input please try again"
            #letterGuessed = raw_input("Please guess a letter: ")
        if lettersGuessed in secretWord and lettersGuessed not in letterlist:
            letterlist += lettersGuessed
            print "Good Guess: "+ str(getGuessedWord(secretWord,letterlist))
        elif lettersGuessed in letterlist:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord,letterlist))
        elif lettersGuessed not in secretWord and lettersGuessed in getAvailableLetters(letterlist):
            letterlist += lettersGuessed
            guesses -= 1
            print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord,letterlist))
        if isWordGuessed(secretWord, letterlist):
            print "-----------"
            return "Congratulations, you won!"
    print "-----------"
    print "Sorry, you ran out of guesses. The word was "+str(secretWord) 
        
        
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = ""
    letterlist = ""
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long"
    #print secretWord
    #print lettersGuessed
    #print getAvailableLetters(lettersGuessed)
    while guesses > 0:
        print "-----------"
        print "You have "+str(guesses)+ " guesses left"
        print "Available letters: "+str(getAvailableLetters(letterlist))
        lettersGuessed = raw_input("Please guess a letter: ")
        lettersGuessed = str(lettersGuessed).lower()
        #if lettersGuessed not in string.ascii_lowercase:
           # print "Opps that was an invalid input please try again"
            #letterGuessed = raw_input("Please guess a letter: ")
        if lettersGuessed in secretWord:
            letterlist += lettersGuessed
            print "Good Guess: "+ str(getGuessedWord(secretWord,letterlist))
        elif lettersGuessed in letterlist:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord,letterlist))
        elif lettersGuessed not in secretWord and lettersGuessed in getAvailableLetters(letterlist):
            letterlist += lettersGuessed
            guesses -= 1
            print "Oops! That letter is not in my word: "+str(getGuessedWord(secretWord,letterlist))
        if isWordGuessed(secretWord, letterlist):
            print "-----------"
            return "Congratulations, you won!"
    print "-----------"
    print "Sorry, you ran out of guesses. The word was "+str(secretWord) 
        
hangman('joe')