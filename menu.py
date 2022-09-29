def begin():
    print('\nВас приветствует телефонный справочник!\n')
    u_choice = input('Выберите:\n1 - Добавить новый контакт\n2 - Показать список контактов\n3 - Выйти из справочника\n')
    print()
    return u_choice  


    
def add_contact():
    print("Введите данные нового контакта")
    name = input('Введите имя: ')
    sorname = input('Введите фамилию: ')
    phone_number = input('Введите номер телефона: ')
    full_contact = (name, sorname, phone_number)
    print('Контакт добавлен!')
    return full_contact