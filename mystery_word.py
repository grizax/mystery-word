import random
import string

with open('/usr/share/dict/words', 'r') as source:
    wordlist = source.read().lower().split()


def choose_word(wordlist):
    '''
    Returns a random word from wordlist
    '''
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string / the word the user is guessing
    letters_guessed: list / which letters have been guessed so far
    returns: boolean / True if all the letters of secret_word
                     are in letters_guessed; False otherwise
    '''
    guessed = True
    letter = 0
    for letter in range(len(secret_word)):
        if secret_word[letter] not in letters_guessed:
            guessed = False
            break
    return guessed


def get_guesssed_word(secret_word, letters_guessed):
    '''
    secret_word: string / the word the user is guessing
    letters_guessed: list / which letters have been guessed
    returns: string /letters and underscores that shows
             which letters in secret_word have been guessed so far
    '''
    letter = 0
    guessed_word = ''
    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            guessed_word = guessed_word + (secret_word[letter] + ' ')
        else:
            guessed_word = guessed_word + ('_ ')
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list / which letters have been guessed
    returns: string / letters that represents which letters have not
             yet been guessed.
    '''
    availableLetters = string.ascii_lowercase
    for letter in letters_guessed:
        if letter in availableLetters:
            remover = availableLetters.partition(letter)
            availableLetters = remover[0] + remover[2]
    return availableLetters


def mystery_word(secret_word):
    '''
    secret_word: string / the word the user is guessing

    '''

    guesses = 8
    letters_guessed = []
    winner = False
    valid_characters = 'abcdefghijklmnopqrstuvwxyz'

    print('''
        **************************************
        *      M Y S T E R Y    W O R D      *
        **************************************
        ''')
    print('Try to guess a word that is ' + str(len(secret_word))
          + ' letters long.')

    while guesses > 0 and winner is False:
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print('You have ' + str(guesses) + ' guesses left!')
        print('Available Letters Remaining: '
              + get_available_letters(letters_guessed))
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter!')
        elif valid_characters.find(guess) < 0:
                print('Please enter a valid letter!')
        elif guess not in get_available_letters(letters_guessed):
            print("Whoops! You've already guessed that letter. Try again: "
                  + get_guesssed_word(secret_word, letters_guessed))
        elif guess not in secret_word:
            letters_guessed.append(guess)
            print('Nope! That letter is not in my word! '
                  + get_guesssed_word(secret_word, letters_guessed))
            guesses -= 1
        elif guess in secret_word:
            letters_guessed.append(guess)
            print('Great guess!            '
                  + get_guesssed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                winner = True

    print('~~~~~~~~~~~~~~~~~~~~~~~')
    if winner is True:
        print('''

                            Congrats! You WON!


                          :                      :M
                         XMX                   .HMM>
                         MMMM.                dMMMM>
                        'MMMMMX     .....   dMMMMMMX
                        XMMMMMMMnMMMMMMMMMMMMMMMMMMM
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMM>
                       XMMMMM!'    'MMMMMM'`  `'MMMMM
                       MMMM#         4MMf        `MMMX
                      XMMM            MX          'MMM:
                     'MMM~            '>            MMM
                     MMMf       .     '>            `MMX
                    MMMM>     :MMM    '>   :MMM      MMMX
                   XMMMM      MMMM>   '>   XMMMX     MMMMk
                  MMMMMM>     MMMM~   'k   MMMMX     MMMMMh
                 MMMMMMMX     XMMM    XX   ?MMM     XMMMMMMM
                 MMMMMMMMk     ^`    X 'h    `     :MM##MMM~
                  ?MM>  ^?M.       .!    %.      .HM'   MM
                 .?M      ''%+++!'.nMMMMn '%++!*' %.. 'M..
                  `?M>+$L         <MMMMMMMM>       :   XM'
                    'X   %        XMMMMMMMM>      X   'f
                      X   `M.      ?MMMMMM~    .HM   :`
                       %.  `MMMx.          .xHMMM   X
                  ..    `X  `MMMMMMMMMMMMMMMMMMM  :f
                :MMMMMMMh:.M. 4MM     '     MM' xMMMMMMMMMMh.
              :MMMMMMMMMMMMMMM: `'x.......x'`.HMMMMMMMMMMMMMM
            .MMMMMMMMMMMMMMMMMMMMhx.......xHMMMMMMMMMMMMMMMMM
    .nHMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`MMMMMMMMMMMMMMMMX
  :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdMMMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMMMMMMMM'``''MMMMMMMMMMMM!MMMMMMMMMMMMMMMMMMMM~
MMMMMMMMMMMMMMMMMMM!     XMMMMMMMMMMMf:HMMMMMMMMMMMMMMMMM!
M?MMMMMMMMMMMMMMMM`    :MMMMMMMMMMMM!MMMMMMMMMMMMMMMMMMM~
:MMMMMMMMMMMMMMMMX     MMMMMMMMMMMMXXMMMMMMMMMMMMMMMMM`
MMMMMMMMMMMMMMMMMX    'MMMMMMMMMMMMM!MMMMMMMMMMMMMMMMX
MMMMMMMMMMMMMMMMM~    'MMMMMMMMMMMMMM?MMMMMMMMMMMMMMM~
 #M)MMMMMMMM!MMM       MMMMMMMMMMMMMMMM/MMMMMMMMMMMM~
   ?MMMMMM'-'2MMMMMx   XMMMMMMMMMMMMMMMMX?**!:MMM'`
     ^''    XMMMMMMMM  'MMMMMMMMMMM'`MMMMMMMMMMM>
           XMMMMMMMMML  MMMMMMMMMX .MMMMMMMMMMMf
           XMMMMMMMMMML 4MMMMMMMMMXMMMMMMMMMMM~
          XMMMMMMMMMMMMXMMMMMMMMMMXMMMMMMMMMx.
            MMMMMMMMMMMMM!MMMMMMMMMMLMMMMMMMMMMMMx
             #MMMMMMMMMMMMMMMMMMMMMMM!MMMMMMMMMMMMM
              `MMMMMMMMMMMLMMMMMMMMMMM/MMMMMMMMMMMM>
                 `*MMMMM!nMMMMMHh(?*MMM?MMMMMMMMMMM>
                       XMMMMMMMMMMMMMMMX4MMMMMMMMMM
                      XM#     `*MMMMMMMMXMMMMMMMM'
                     'M          `MMMMMMMX^'*''
                     Xf            !?MMMMMM
                     'X             X ?MMMMM
                      !             `> `MMMMX
                       #:     4     X>  'MMMM>
                        `L     'x.xM~    `MMMX
                          %.    f         MMMX
                           `#M``         :MMM~
                              `Mx.      dMMM~
                                 ``'**MM*
            ''')
    else:
        print('Sorry, the word was ' + secret_word + '.'
              '''



                          ,;|||||\                       ____________
       ___               |;|||:;:|                    ,'      You   |---.
      /;,a.\ \             |||||...._                   `-. _    LOSE!   ;
      |||@@@\ \        __----,'......~\_    ,---._        ;; `-._______,'
      |||@@@@\ \,-~~~~::::::,'... _.----\_,'      `.      '
      |||;aaa/,;;;;:::::::::: _.-':      ;...._    ;
      `::||||;;;;:::::::::::' `--'    ,;;:::::~:~~----._____
           ;;;;;::::::::::::`-.     ,;::::::::::::::::::::::::___
          |;;;;;:::::::::::::::`---;:::::::::::::::::::'.,-/~~   ~~\-._
          |;;;;;;;;:::::::::::::::::::::::::::::::::',-'   `\  |  /'.  :
           `-:;;;;;;;;;;::::::::::::::::::::::::::::;  . .   `\:/' . . ;
              `~--;;;;;;;;;;;;::::::::::::::::::::::: . .      |     ,'
                  `~~~~--;;;;;;;;;;;;::::::::::::::::`..    _/' `\_/';
                         `~~.;;;;;::::::::::::::::::::::---' . ..   ,'
                             ~~;.....;'~~~`---.::::::::::         ,'
                               :;;;:::         ~~~~~~`---`-.____,'
                               `|;;::::
                                |;;:::::                   ...........
                                |;;:::::                 .::::::::::|||:.
                             ___||::::::: ___           .||||        `:|||
                           /':::`|::::::|':::`\        .||||          ||||
                          /::::::||/@@@\::::::::\      ||||           ||||
                         /::::::||:@@@@@@@\::::::\     ||||__         ||||
                        /::::::|||@@@@@@@@@|::::::\    |`.`--)        ||||
                       /::::::;||:@@@@@@@@@|:::::::\    \_~_/        ,||||
                      /:::::;;|||:@@@@@@@@@@|\::::::\                ||||'
                     /:::::;;;||::@@@@@@@@@@| \::::::\               ||||
                    /:::::;; |||:@@@@@@@@@@@@| \::::::\              ||||.
                   /:::::;;  |||:@@@@@@@@@@@@|. \::::::\             `||||
                  ,'::::;;  |||::@@@@@@@@@@@@||  \::::::\___          ||||
                 ,:::::;;   |||::@@@@@@@@@@@|:|   \;,'~~'_  `-.      ,||||
                ,:::::;;    ||::@@@@@@@@@@@@|:|   ,'   ~~ `._  `.   ,||||'
               ,::::;;;    |||::_--._@@@@@@|::| ,'     __    `._|  .||||'
              ,:::::;;     ;~~~'     ~--.__|::|;      '  `-.   ;   ||||'
             ,::::;;;    ,'        ::::::::~~--;__          `_,'   |||||
            ,:::::;;   ,'         (~--::::::::::: ~~-._    _;\     `|||||
           ,:::::;/  ,'   _______-.-----~~~-._ ::::::  `--' ;;\     `|||||
          |:::::/  ____.-:::::::::::::::::::,-~-.::::::::::::::)    .||||'
          |:::::`~':::::::::::::::::::.--'|::::| `~~~~~--.__.-'     ||||'
          `::::::::::::::::___----~~~~@@@@|::::|                 .|||||'
           `--____,---~~~~~   @@@@@@@@@@@|:::::|                ,||||.'
                  ;          `.@@@@@@@@@@|:::::|            ,||||||.'
                 |  :   :     ;@@@@@@@@@@|:::::|         ,|||||||.'
                 `._;.__;`-._,'@@@@@@@@@@|:::::|      ,|||||||'~~
                        |:@@@@@@@@@@@@@@|:::::::|   ,||||||'~
                        |:@@@@@@@@@@@@@@|:::::::|  ||||||'
      =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

            ''')


'''ASCII art found at: http://www.asciiworld.com/'''


secret_word = choose_word(wordlist).lower()
mystery_word(secret_word)
