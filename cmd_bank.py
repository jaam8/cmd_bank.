import json


# TOOLS FUNCTIONS

def load_data() -> list:
    '''выгружает и возвращает данные из файла'''
    try:
        with open('list_users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def add_user(data: list, new_user) -> list:
    '''добавление юзера'''
    data.append(new_user)
    return data


def save_data(data: list) -> None:
    '''вгружает данные в файл'''
    with open('list_users.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def update_data_user(data: list, user_id: dict, key_for_value: str, mutable_value: str | int) -> None:
    '''обновляет необходимые значения в словаре юзера'''
    for user in data:
        if user['id'] == user_id:
            user[key_for_value] = mutable_value
    save_data(data)


def search_user(search_key, comparative_string) -> dict:
    '''поиск нужного значения в словаре пользователя'''
    list_users = load_data()
    for x in list_users:
        if x[search_key] == comparative_string:
            return x
    else:
        raise TypeError


# MAIN FUNCTIONS

def registration() -> None:
    '''регистрация пользователя'''
    name_user = input('for registration enter your firstname and lastname\n')
    country_user = input('enter your country of residence\n')
    phone_number = input('enter your phone number\n')
    password = input('come up and enter your password\n')
    data_user = {
                'id': len(load_data())+1,
                'name': (*name_user.split(),),
                'country': country_user,
                'phone number': phone_number,
                'password': password,
                'balance': 0
                }
    save_data(add_user(load_data(), data_user))


def authentication() -> dict | TypeError | None:
    '''выводит результат поиска данных для входа в консоль'''
    try:
        phone_number_search = input('enter your number phone\n')
        search_user('phone number', phone_number_search)
        verification_password = input('enter your password\n')
        x = search_user('password', verification_password)
        print(f'hay {x['name'][0]}')
        return x
    except TypeError:
        print('that user is unfounded :-(')
    except:
        print('something went wrong :(')


def top_up_balance(data_user) -> None:
    '''пополняет баланс юзера'''
    top_up_sum = int(input('enter the amount for which you want to top up the balance\n'))
    new_value = data_user['balance'] + top_up_sum
    print(f'your balance {data_user['balance']}')
    update_data_user(load_data(), data_user['id'], 'balance', new_value)


def money_transfer(data_user):
    '''переводит средства от одного юзера к другому'''
    recipient_num = input('enter recipient number\n')
    recipient = search_user('phone number', recipient_num)
    transfer_amount = int(input('enter amount for recipient\n'))
    new_value_user = data_user['balance'] - transfer_amount
    new_value_recipient = recipient['balance'] + transfer_amount
    update_data_user(load_data(), data_user['id'], 'balance', new_value_user)
    update_data_user(load_data(), recipient['id'], 'balance', new_value_recipient)


# MENU COMMANDS

while True:
    user_text = input('r - registration\nl - log in\ntb - top-up balance\nmt - money transfer\ns - stop\n')
    if user_text == 'r':
        registration()
        print('done')
        break
    elif user_text == 'l':
        data_user = authentication()
    elif user_text == 'tb':
        top_up_balance(data_user)
    elif user_text == 'mt':
        money_transfer(data_user)
    elif user_text == 's':
        print('see you again')
        break
    else:
        print('i dont know this command')
