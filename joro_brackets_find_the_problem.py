lines = int(input())

bracket_orientation = ''
bracket_left = 0
bracket_right = 0
bracket_position = 0

for i in range(1, lines + 1):

    string = input()

    if string != '(' and string != ')':
        continue

    if string == ')' and bracket_orientation == '':
        print('UNBALANCED')
        break

    elif string == '(' and bracket_orientation == '':
        bracket_orientation = '('
        bracket_position = i
        continue

    if string == ')' and bracket_orientation == '(':
        if i == bracket_position + 2:
            bracket_position += 2
            bracket_orientation = ')'

            continue

        else:
            print('UNBALANCED')
            break

    elif string == '(' and bracket_orientation == ')':
        if i == bracket_position + 2:
            bracket_position += 2
            bracket_orientation = '('

            continue

        else:
            print('UNBALANCED')
    else:
        print('UNBALANCED')
        break
else:
    print('BALANCED')
