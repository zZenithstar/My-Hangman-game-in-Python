import random
#With these codes, we will randomly select a word from a specific list,
#and we will be given as many chances as the number of heads, arms, and legs of
#a man to guess the word.simply is a hangman game.


manPic1 = [["--------",#these are picture of the man
          "   |  ",
          "   0 ",
          " / | \\ ",
          "  | |"],
          ["--------",
          "   |  ",
          "   0 ",
          " / | \\ ",
          "  | "],
          ["--------",
          "   |  ",
          "   0 ",
          " / | \\ "
           ],
          ["--------",
          "   |  ",
          "   0 ",
          " / |  "],

          ["--------",
          "   |  ",
          "   0 ",
          "   |  "],

         ["--------",
          "   |  ",
          "   0 "]]




wordSecret = "" #We can hide the word with this
wordList = ["portakal","elma","muz","kiraz","çilek","karpuz","mandalina"]#words(only fruit you can change)
randomWord = random.choice(wordList)#random word choice
wordLength = len(randomWord)# word lenght


for x in range(wordLength):
    wordSecret += "-"#hiding

a = 0
running = True
while running:
    if a < 6:
        for i in manPic1[a]:
            print(i)
        print()
        print(wordSecret)
        print(wordLength, "Characters")
    else:#lost stiuation
        print("YOU LOST!")
        print("YOUR WORD İS: ", randomWord.upper())
        break

    userChoice = input("Enter your character: ")
    userChoice = userChoice.lower()

    if userChoice in randomWord:
        newCharfind = randomWord.index(userChoice)
        wordSecret = wordSecret.replace(wordSecret[newCharfind], userChoice,1)
        print(wordSecret)
    else:
        a += 1

    if wordSecret == randomWord:# win stuiation
        print("YOU WIN!")
        running = False
