#1-skilgreina breytur x_cord og y_cord. Og input option 
#2-while loop  með if statements innbyrgðis
#3-Victory!
#linkur a git ()

#upphafshnit skilgreind
x_cord,y_cord = 1,1

def tile(x,y):
    return x_cord == int(x) and y_cord==int(y) 
def opening(letter,word):
    if is_open[i] == letter:
        print(word, end='')
def add(cord, letter):
    if to_direction == letter:
        cord += 1
        return cord
        
def subtr(cord, letter):
    if to_direction == letter:
        cord -= 1
        return cord

#byrjun a loop-u 
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
        opening('e','(E)east')
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
        add(y_cord, 'n')
        subtr(y_cord, 's')
        subtr(x_cord, 'w')
        add(x_cord, 'e')
else: 
    print('Victory!')