def user_info(surname, name, birth_y, location, email, phone_num):
    print(f'{name} {surname}, {birth_y} года рождения, место проживания: {location}, электронная почта: {email},\xa0'
          f'контактный номер: {phone_num}.')


user_info(surname=input("Введите фамилию: "),
          name=input("Введите имя: "),
          birth_y=int(input("Введите год рождения: ")),
          location=input("Введите место проживания: "),
          email=input("Введите email: "),
          phone_num=int(input("Введите номер телефона: ")))
