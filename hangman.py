import random
def hangman():
    list_of_words=['harrypotter','wizard','ginny','hermione','dumbledore','voldemort']
    word=random.choice(list_of_words)
    turns=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=''
        
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_"
        if main_word==word:
            print(main_word)
            print("you won!")

        print("Guess the word",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid charcter")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("you have 9 turns left!")
            elif turns==8:
                print("you have 8 turns left!")
            elif turns==7:
                print("you have 7 turns left!")
            elif turns==6:
                print("you have 6 turns left!")
            elif turns==5:
                print("you have 5 turns left!")
            elif turns==4:
                print("you have 4 turns left!")
            elif turns==3:
                print("you have 3 turns left!")
            elif turns==2:
                print("you have 2 turns left!")
            elif turns==1:
                print("you have 1 turns left!")
            elif turns==0:
                print("you loose!")
                break
    

name=input("enter your name:")
print("Welcome!",name)
print("Try to guess the word in less than 10 attempts")
hangman()
