#1-skilgreina breytur x_cord og y_cord. Og input option 
#2-while loop  með if statements innbyrgðis
#3-Victory!
#linkur a git ()

#upphafshnit skilgreind
x_cord,y_cord = 1,1

#byrjun a loop-u 
while x_cord != 3 or y_cord != 1:
    if (x_cord == 1 and y_cord == 1) or (x_cord == 2 and y_cord == 1):
        is_open = 'n'
    elif x_cord == 1 and y_cord == 2:
        is_open = 'nes'
    elif x_cord == 1 and y_cord == 3:
        is_open = 'es'
    elif x_cord == 2 and y_cord == 2:
        is_open = 'sw'
    elif x_cord == 2 and y_cord == 3:
        is_open = 'ew'
    elif x_cord == 3 and y_cord == 3:
        is_open = 'sw'
    elif x_cord == 3 and y_cord == 2:
        is_open = 'ns'
        
    print('You can travel:', end=' ')
        
    for i in range(len(is_open)):
        if i > 0:
            print('or',end=' ') 

        if is_open[i] == 'n':
            print('(N)orth', end='')
        elif is_open[i] == 's':
            print('(S)outh', end='')
        elif is_open[i] == 'e':
            print('(E)ast', end='')
        elif is_open[i] == 'w': 
            print('(W)est', end='') 
        if i == len(is_open) - 1: 
            print('.')
        else:
            print(' ', end='')

    to_direction = input('Direction: ')
    to_direction = to_direction.lower()
    while to_direction not in is_open:
            print('Not a valid direction!')
            to_direction = input('Direction: ')
            to_direction = to_direction.lower()

    else:
        if to_direction == 'n':
            y_cord += 1
            continue
        elif to_direction == 's':
            y_cord -= 1
            continue
        elif to_direction == 'w':
            x_cord -= 1
            continue
        elif to_direction == 'e':
            x_cord += 1
            continue
else: 
    print('Victory!')