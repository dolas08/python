def info(name, surname, year, state, email, phone):
    """
    :param name: string with name
    :param surname: string with surname
    :param year: string with year
    :param state: string with sity
    :param email: string with email
    :param phone: string with phone number
    :return: sum all strings
    """
    my_str = name + ' ' + surname + ' ' + year + ' ' + state + ' ' + email + ' ' + phone
    print(my_str)


my_name = input("Ваше имя: ")
my_surname = input("Ваша фамилия: ")
my_year = input("Ваш год рождения: ")
my_state = input("Ваш город: ")
my_email = input("Ваш email: ")
my_phone = input("Ваш номер телефона: ")
info(my_name, my_surname, my_year, my_state, my_email, my_phone)
