# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = 'words.txt'


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_set=set(secret_word)
    letters_guessed=set(letters_guessed)
    return secret_word_set==letters_guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed=list(letters_guessed)
    secret_word=list(secret_word)
    my_word=str()
    for item in secret_word:
        if item in letters_guessed:
            my_word += item
        else:
            my_word += ('_ ')
    return my_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_guessed=list(letters_guessed)
    all_letters=list(string.ascii_lowercase)
    r_letters=str()
    for item in all_letters:
        if item in letters_guessed:
            item=''
        else:
            r_letters += item
    return r_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    n_guesses=6
    n_warning=3
    letters_input=''
    letters_guessed=''
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + 
    str(len(set(secret_word))) + ' letters long. ' +
    str(get_guessed_word(secret_word, letters_guessed)))
    
    while not is_word_guessed(secret_word, letters_guessed):
      if n_guesses >=0:
        print('You have ' + str(n_guesses) + ' guesses left.')
        print('Available letters: ' + str(get_available_letters(letters_guessed)))
        letters_input = str.lower(input('Please guess a letter: '))
      else:
        break
      if str.isalpha(letters_input)==True and len(letters_input)==1 and (letters_input in letters_guessed)==False:
        letters_guessed += letters_input
        if letters_input in secret_word:
          print('Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-'*10)
        else:
          if letters_input in ('a', 'e', 'i', 'o', 'u'):
            n_guesses -= 2
          else:
            n_guesses -= 1
          print('Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-'*10)
      else:
        if n_warning >= 1:
          n_warning -= 1
          print('Oops! That is not a valid letter. You have ' + str(n_warning) + ' warnings left: ' + str(get_guessed_word(secret_word, letters_guessed)))
        else:
            n_guesses -= 1
            print('Oops! That is not a valid letter. You have ' + 
            str(n_warning) + ' warnings left, you losing 1 guesses, ' + str(n_guesses) + ' guesses left: ' + 
            str(get_guessed_word(secret_word, letters_guessed)))
    if n_guesses <= 0:
      print('Sorry, you ran out of guesses. The word was ' + str(secret_word))
    else:
      score=n_guesses*int(len(set(secret_word)))    
      print('Congratulations, you won!\nYour total score for this game is: ' + str(score))

        




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word=my_word.split(' ')
    my_word=''.join(my_word)
    a=''
    if len(my_word)==len(other_word):
          for i in range(0, len(my_word)):
                if my_word[i] == '_':
                      a += other_word[i]
                else:
                      a += my_word[i]
    else:
          return False            
    return a==other_word



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    show_matches=str()
    for item in wordlist:
      if match_with_gaps(my_word, item)==True:
        show_matches += ' ' + item
      else:
        continue
    if len(show_matches)==0:
      print('No matches found')
    elif len(show_matches):
      print(show_matches) 



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    n_guesses=6
    n_warning=3
    letters_input=''
    letters_guessed=''
    print('Welcome to the game Hangman!\nI am thinking of a word that is ' + 
    str(len(set(secret_word))) + ' letters long. ' +
    str(get_guessed_word(secret_word, letters_guessed)))
    
    while not is_word_guessed(secret_word, letters_guessed):
      if n_guesses >= 0:
        print('You have ' + str(n_guesses) + ' guesses left.')
        print('Available letters: ' + str(get_available_letters(letters_guessed)))
        letters_input = str.lower(input('Please guess a letter: '))
      else:
        break
      if letters_input == '*':
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        print('-'*10)
      elif str.isalpha(letters_input) == True and len(letters_input) == 1 and letters_input not in letters_guessed:
        if letters_input in secret_word:
          letters_guessed += letters_input
          print('Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-'*10)
        else:
          if letters_input in ('a', 'e', 'i', 'o', 'u'):
            n_guesses -= 2
          else:
            n_guesses -= 1
          print('Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-'*10)
      else:
        if n_warning >= 1:
          n_warning -= 1
          print('Oops! That is not a valid letter. You have ' + str(n_warning) + ' warnings left: ' + str(get_guessed_word(secret_word, letters_guessed)))
        else:
            n_guesses -= 1
            print('Oops! That is not a valid letter. You have ' + 
            str(n_warning) + ' warnings left, you losing 1 guesses, ' + str(n_guesses) + ' guesses left: ' + 
            str(get_guessed_word(secret_word, letters_guessed)))
    if n_guesses >= 0:
      score=n_guesses*int(len(set(secret_word)))    
      print('Congratulations, you won!\nYour total score for this game is: ' + str(score))
    else:
      print('Sorry, you ran out of guesses. The word was ' + str(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
