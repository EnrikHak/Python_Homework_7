def contact_log(full_contact):

    name, sorname, phone_number = full_contact
    with open('spisok.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{sorname} {name} тел. {phone_number}\n')
