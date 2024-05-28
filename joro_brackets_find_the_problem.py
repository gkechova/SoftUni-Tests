lines = int(input())

bracket_orientation = ''
bracket_position = 0

for i in range(1, lines + 1):

    string = input()

    if string == ')' and bracket_orientation == '':
        print('UNBALANCED')
        break

    if string == '(' and bracket_orientation == "(":
        print('UNBALANCED')
        break

    if string == '(' and bracket_orientation == '':
            bracket_orientation = '('
            bracket_position = i

    if string == ')' and bracket_orientation == '(':
        if i > bracket_position:
            bracket_position = i
            bracket_orientation = ''

else:
    print('BALANCED')
    
