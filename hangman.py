import time

name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman wait for 1 second"
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

word = "secret"

guesses = ''


turns = 10



while turns > 0:         

    failed = 0             

    for char in word:      

        if char in guesses:    
    
            print char,    

        else:
    
            print "_",     
       
            failed += 1    


    if failed == 0:        
        print "You won"  

  
        break              

    print

    
    guess = raw_input("guess a character:") 

    
    guesses += guess                    

    if guess not in word:  
 
        turns -= 1
        print "Wrong"    
 
        print "You have", + turns, 'more guesses' 
 
        if turns == 0:           
    
            print "You Lose"














'''
output:

1.What is your name? nithish
Hello, nithish Time to play hangman wait for 1 second
Start guessing...
_ _ _ _ _ _
guess a character:e
_ e _ _ e _
guess a character:s
s e _ _ e _
guess a character:c
s e c _ e _
guess a character:r
s e c r e _
guess a character:t
s e c r e t You won'''
'''
2.What is your name? nith
Hello, nith Time to play hangman wait for 1 second
Start guessing...
_ _ _ _ _ _
guess a character:t
_ _ _ _ _ t
guess a character:s
s _ _ _ _ t
guess a character:e
s e _ _ e t
guess a character:f
Wrong
You have 9 more guesses
s e _ _ e t
guess a character:t
s e _ _ e t
guess a character:v
Wrong
You have 8 more guesses
s e _ _ e t
guess a character:s
s e _ _ e t
guess a character:v
Wrong
You have 7 more guesses
s e _ _ e t
guess a character:j
Wrong
You have 6 more guesses
s e _ _ e t
guess a character:t
s e _ _ e t
guess a character:b
Wrong
You have 5 more guesses
s e _ _ e t
guess a character:j
Wrong
You have 4 more guesses
s e _ _ e t
guess a character:d
Wrong
You have 3 more guesses
s e _ _ e t
guess a character:m
Wrong
You have 2 more guesses
s e _ _ e t
guess a character:c
s e c _ e t
guess a character:g
Wrong
You have 1 more guesses
s e c _ e t
guess a character:j
Wrong
You have 0 more guesses
You Lose'''



