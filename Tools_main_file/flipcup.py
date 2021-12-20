cups = '~  ~  ~  ~  ~  ~  ~  ~  ~'
num = 0, 3, 6, 9, 12, 15, 18, 21, 24
# ['`', '`', '`', '`', '`', '`', '`', '`', '`']

print(cups)
while cups != '_  _  _  _  _  _  _  _  _':
    change = input("\nWhich six?:\t\t")
    count = 0
    before = cups
    for x in change:
        count += 1
        x = int(x)*3-3
        char = '_'
        
        if cups[x] == char:
            char = '~'
        
        cups = cups[:x] + char + cups[x+1:]

    if count != 6:
        print("\nyou didn't enter 6 number correctly")
        cups = before
    else:
        print('\n\n\n')
        print('1  2  3  4  5  6  7  8  9')
        print(cups)
