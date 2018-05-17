import random
print ('this is a rock paper scissors game')
while True:
    playersThrow = input('so whats it gonna be?')

    while playersThrow != 'rock' and playersThrow != 'paper' and playersThrow != 'scissors':
        print ('incorrect choice - try again')
        playersThrow = input('so whats it gonna be?')

    computersThrow = random.choice (['rock', 'paper', 'scissors'])
    print ('This is the players throw',playersThrow)
    print ('This is the computers throw',computersThrow)

    if computersThrow == playersThrow:
        print ('draw!')
    if computersThrow == 'rock' and playersThrow == 'paper':
        print ('you win!')
    if computersThrow == 'rock' and playersThrow == 'scissors':
        print ('you lose')
    if computersThrow == 'paper' and playersThrow == 'scissors':
        print ('you win!')
    if computersThrow == 'paper' and playersThrow == 'rock':
        print ('you lose')
    if computersThrow == 'scissors' and playersThrow == 'paper':
        print ('you win!')
    if computersThrow == 'scissors' and playersThrow == 'rock':
        print ('you lose')
    carryon = input('do you want to carry on?')
    if carryon == 'no':
        print ('ok see you next time')
        break
            
    
           


