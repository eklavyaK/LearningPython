import os
import time
import sys


def clear():
    os.system('cls')


i = 0
j = 0
boolean = True
list1 = [' ', ' ', ' ']
list2 = [' ', ' ', ' ']
list3 = [' ', ' ', ' ']
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def initial():
    global list1
    global list2
    global list3
    global list4
    list1 = [' ', ' ', ' ']
    list2 = [' ', ' ', ' ']
    list3 = [' ', ' ', ' ']
    list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def result_check(user_choice):
    global list1
    global list2
    global list3
    global j
    j = 0
    for a in list1:
        if user_choice == a and user_choice != ' ':
            j = j + 1
            if j == 3:
                return 1
    j = 0
    for a in list2:
        if user_choice == a and user_choice != ' ':
            j = j + 1
            if j == 3:
                return 1
    j = 0
    for a in list3:
        if user_choice == a and user_choice != ' ':
            j = j + 1
            if j == 3:
                return 1
    for a in range(3):
        if list1[a] == user_choice and list2[a] == user_choice and list3[a] == user_choice and user_choice != ' ':
            return 1
        if list1[0] == user_choice and list2[1] == user_choice and list3[2] == user_choice and user_choice != ' ':
            return 1
        if list1[2] == user_choice and list2[1] == user_choice and list3[0] == user_choice and user_choice != ' ':
            return 1
    return 0


def display_matrix(user_choice):
    global list1
    global list2
    global list3
    print("      {} | {} | {}                                 1 | 2 | 3 ".format(
        list1[0], list1[1], list1[2]))
    print('   ---------------                           ---------------           This represents')
    print("      {} | {} | {}                                 4 | 5 | 6     <------  the index positions".format(
        list2[0], list2[1], list2[2]))
    print('   ---------------                           ---------------           of the cells')
    print("      {} | {} | {}                                 7 | 8 | 9 ".format(
        list3[0], list3[1], list3[2]))
    print('\n')
    m = result_check(user_choice)
    return m


def user_response(value, user_choice):
    global list1
    global list2
    global list3
    if int(value) in [1, 2, 3]:
        list1[int(value) - 1] = user_choice
    if int(value) in [4, 5, 6]:
        list2[int(value) - 4] = user_choice
    if int(value) in [7, 8, 9]:
        list3[int(value) - 7] = user_choice
    m = int(display_matrix(user_choice))
    return m


def print_result(n, k):
    if n == 1:
        print('Congrats ' + k + '! You have won.')
        print(
            '--------------------------------------------------------------------------\n')
        user_interaction()

    elif n == 2:
        user_interaction()
    else:
        print('Match draw')
        print(
            '--------------------------------------------------------------------------\n')
        user_interaction()


def the_game(a, b, y, z):
    global boolean
    global list4
    boolean = True
    while boolean == True:
        value = str(input(
            '{} enter the cell position where you want to put your {}:\n'.format(a, y)))
        if value.isdigit() and int(value) in range(1, 10) and int(value) in list4:
            list4.remove(int(value))
            boolean = False
            clear()
            print('\n')
            m = user_response(value, y)
            if (m == 1):
                print_result(1, a)
                break
        else:
            print(
                'Invalid choice\n------------------------------------------------------')
            print('\n')
            boolean = True
    while boolean == False:
        if i == 4:
            break
        value = str(input(
            '{} enter the cell position where you want to put your {}:\n'.format(b, z)))
        if value.isdigit() and int(value) in range(1, 10) and int(value) in list4:
            list4.remove(int(value))
            boolean = True
            clear()
            print('\n')
            m = user_response(value, z)
            if (m == 1):
                print_result(1, b)
                break
        else:
            print(
                'Invalid choice\n------------------------------------------------------')
            print('\n')
            boolean = False


def user_assignment(a, b, y, z):
    global list1
    global list2
    global list3
    global i
    time.sleep(5)
    clear()
    print('\n')
    m = user_response(1, ' ')
    i = 0
    while i in range(5):
        the_game(a, b, y, z)
        i = i + 1
    print_result(0, ' ')


def user_interaction():
    initial()
    x = str(input(
        'Press y from the keyboard if you want to play the game or press n to exit: '))
    print('\n')
    if x.lower() == 'y':
        a = str(input('Name of Player 1: '))
        print('\n')
        b = str(input('Name of Player 2: '))
        print('\n')
        user_choice = ' '
        m = user_response(1, user_choice)
        g = True
        while (g == True):
            print('\n')
            y = str(input('{} choose your symbol(x or o): '.format(a)))
            if y.lower() == 'x':
                z = 'o'
                print('\n')
                print('Symbol for {} is: {}'.format(b, z))
                print('\n')
                print('Wait for 5 seconds for game to start')
                user_assignment(a, b, y, z)
                g = False
            elif y.lower() == 'o':
                z = 'x'
                print('\n')
                print('Symbol for {} is: {}'.format(b, z))
                print('\n')
                print('Wait for 5 seconds for game to start')
                user_assignment(a, b, y, z)
                g = False
            else:
                print('\n')
                print("Invalid input")
                print(
                    '--------------------------------------------------------------------------\n')
                g = True
    elif x.lower() == 'n':
        sys.exit()
    else:
        print("Invalid choice")
        print(
            '--------------------------------------------------------------------------\n')
        print_result(2, ' ')


user_interaction()
