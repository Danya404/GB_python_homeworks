# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import os


def show_contacts(file_name):
    os.system('cls')
    with open(file_name, 'r') as f:
        data = f.readlines()

        for contact in data:
            print(contact, end='')
    input('\npress any key')


def add_contact(file_name):
    os.system('cls')
    with open(file_name, 'a') as f:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')
        f.write('\n' + res)
    input('Contact was successfully added. Press any key for return')


def search_contact(file_name):
    os.system('cls')
    target = input('Input a name for searching: ')
    with open(file_name, 'r') as f:
        contacts = f.readlines()

        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print('There is no contacts with such name')
    input('press any key')


def change_contact(file_name):
    os.system('cls')
    target = input('Input a name for searching: ')
    with open(file_name, 'r') as f:
        contacts = f.readlines()
    print(contacts)

    for contact in contacts:
        if target in contact:
            print(contact)
            res = ''
            res += input('Input a new surname of contact: ') + ' '
            res += input('Input a new name of contact: ') + ' '
            res += input('Input a new phone number of contact: ')
            contacts[contacts.index(contact)] = res + '\n'
            with open(file_name, 'w') as f:
                for line in contacts:
                    f.writelines(line)
            input('Contact was successfully changed. Press any key for return')
            break

    else:
        print('There is no contacts with such name')



def delete_contact(file_name):
    os.system('cls')
    target = input('Input a name for searching: ')
    with open(file_name, 'r') as f:
        contacts = f.readlines()

    for contact in contacts:
        if target in contact:
            confirmation = input('Are you sure you want to delete this contact?(y/n)')
            if confirmation == 'y':
                contacts[contacts.index(contact)] = ''.strip()
                with open(file_name, 'w') as f:
                    for line in contacts:
                        f.writelines(line)
                input('Contact was successfully deleted. Press any key for return')
                break
            else:
                input('Good for him/her. Press any key for return')

    else:
        print('There is no contacts with such name')


def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - change contact')
    print('5 - delete contact')
    print('6 - exit')


def main(file_name):
    while True:
        os.system('cls')
        drawing()
        user_choice = int(input('Select an action: '))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            change_contact(file_name)
        elif user_choice == 5:
            delete_contact(file_name)
        elif user_choice == 6:
            print('Have a nice day!')
            return


main('phonebook.txt')
