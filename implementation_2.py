#1-skilgreina breytur x_cord og y_cord. Og input option 
#2-while loop  með if statements innbyrgðis
#3-Victory!
#linkur a git ()
#1. seinni var auðveldari þar sem kóðinn er styttri og mun viðráðanlegri þegar hann er skoðaður
#2. Seinni er lesanlegri vegna þess að hann er 8x styttri og ekki jafn mikil endurtekning 
#3.kóðinn varð lesanlegri og endurtekningum var fækkað áttfallt.

#upphafshnit skilgreind
x_cord,y_cord = 1,1
#functions skilgreindir
def tile(x,y):
    return x_cord == int(x) and y_cord==int(y) 
def opening(letter,word):
    if is_open[i] == letter:
        print(word, end='')

#byrjun a loop-u ath! functions notad
while x_cord != 3 or y_cord != 1:

    if tile(1,1) or tile (2,1):
        is_open = 'n'
    elif tile(1,2):
        is_open = 'nes'
    elif tile(1,3):
        is_open = 'es'
    elif tile(2,2):
        is_open = 'sw'
    elif tile(2,3):
        is_open = 'ew'
    elif tile(3,3):
        is_open = 'sw'
    elif tile(3,2):
        is_open = 'ns'
        
    print('You can travel:', end=' ')       
    for i in range(len(is_open)):
        if i > 0:
            print('or',end=' ') 
        
        opening('n','(N)orth')
        opening('e','(E)ast')
        opening('s','(S)outh')
        opening('w','(W)est')
        if i == len(is_open) - 1:
            print('.')
        else:
            print(' ', end='')
    to_direction = input('Direction: ').lower()
    while to_direction not in is_open:
            print('Not a valid direction!')
            to_direction = input('Direction: ').lower()

    else:
        if to_direction == 'n':
            y_cord += 1
            continue
        if to_direction == 's':
            y_cord -= 1
            continue
        if to_direction == 'w':
            x_cord -= 1
            continue
        if to_direction == 'e':
            x_cord += 1
            continue 
else: 
    print('Victory!')