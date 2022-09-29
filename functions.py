from menu import begin, add_contact
from log import contact_log


def add_new_full_contact():
    full_contact = add_contact()
    contact_log(full_contact)



def print_spisok():
    print('Ваш телефонный справочник:')
    with open('spisok.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)


def click_button():
    u_choice = begin()
    if u_choice == '1':
        add_new_full_contact()
    elif u_choice == '2':
        print_spisok()
    elif u_choice == '3':
        print('Телефонный справочник с Вами прощается!')
    else:
        print('Если ввели некоректно, нажмите кнопку еще раз, чтобы начать сначала')
