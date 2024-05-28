lines = int(input())
bracket_orientation = ''

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

    if string == ')' and bracket_orientation == '(':
            bracket_orientation = ''

else:
    print('BALANCED')
    
