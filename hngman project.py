###hangman project
import random
def hangman():
    list_word=["eduyear","hangman","india","laptop"]
    word=random.choice(list_word)
    print(word)
    turns=10
    guessmade= ''
    valid_entry=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=""
        missed=0
        
        for lettter in word:
            if lettter in guessmade:
                main_word = main_word+lettter
            else:
                main_word = main_word+"_"
        if main_word==word:
            print(main_word)
            print("you win!!!!")
            break
        print("guess the word",main_word)
        guess=input()
        if guess in valid_entry:
            guessmade=guessmade+guess
        else:
            print("enter valid character")

            guess=input()
        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left!!")
                print("---------------")
            if turns==8:
                print("8 turns left!!")
                print("---------------")
                print("       0        ")
            if turns==7:
                print("7 turns left!!")
                print("---------------")
                print("       0        ")
                print("       |        ")
            if turns==6:
                print("6 turns left!!")
                print("---------------")
                print("       0        ")
                print("       |        ")
                print("      /         ")
            if turns==5:
                print("5 turns lest!!")
                print("---------------")
                print("       0       ")
                print("       |       ")
                print("      / \       ")   
            if turns==4:
                print("4 turns lest!!")
                print("---------------")
                print("      \0        ")
                print("       |        ")
                print("      / \       ")
            if turns==3:
                print("3 turns lest!!")
                print("---------------")
                print("      \0/       ")
                print("       |        ")
                print("      / \       ")
            if turns==2:
                print("2 turns lest!!!")
                print("---------------")
                print("      \0/ |    ")
                print("       |       ")
                print("      / \      ")
        
            if turns==1:
                print("only 1 turn left!!!hang man on his last breath")
                print("---------------")
                print("      \0/_|    ")
                print("       |       ")
                print("      / \      ")
            if turns==0:
                print("you losse")
                print("you let a good man die")
                print("       0_|   ")
                print("      /|\     ")
                print("      / \     ")
                break
name=input("enter name:")
print("well come",name)
print("--------------------------")
print("try to guess word in less then 10 attempts!")
hangman()
