import random

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ==='''
]

list = [
    "Serendipity", "Petrichor", "Supine", "Aurora", "Idyllic", "Pluviophile",
    "Euphoria"
]
index = random.randint(0, len(list) - 1)
wor = list[index]
word = wor.lower()
actual_word = []
for i in word:
  actual_word.append("_")
end_of_the_game = False
lives = 7
while not end_of_the_game:
  print("Guess a letter of the word ")
  Guess_wor = input()
  Guess_word = Guess_wor.lower()
  count = 0
  for i in word:
    if (i == Guess_word):
      actual_word[count] = i
    count += 1
  if Guess_word in word:

    print(actual_word)
  else:
    lives -= 1
    print(HANGMAN_PICS[6 - lives])
  if "_" not in actual_word:
    end_of_the_game = True
  if (lives == 0):
    print("YOU LOST")
    break
if "_" not in actual_word:
  print("You Win")
