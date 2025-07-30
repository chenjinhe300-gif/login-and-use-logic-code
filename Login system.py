from random import randint
import random
import string

def generate_username(length=8):
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choices(characters, k=length))
    return username  
def progress_bar():
    from time import sleep
    for i in range(0, 101):
        print(f'\r正在处理... {i}%', end='')
        sleep(sleep)
        return sleep
    print('\n处理完成！')
def check_username(name):
    while True:
        if isinstance(name, str) and len(name) > 0:
            return name
        else:
            print('昵称输入有误，请重新输入')
def check_password(password):
    while True:
        if isinstance(password, str) and len(password) >= 6:
            return password
        else:
            print('密码输入有误，请重新输入')
def check_confirm(confirm, password):
    while True:
        if confirm == password:
            return confirm
        else:
            print('两次密码输入不一致，请重新输入')
def progress_bar(sleep_time):
    from time import sleep
    for i in range(0, 101):
        print(f'\r正在处理... {i}%', end='')
        sleep(sleep_time)
    print('\n处理完成！')
print('请输入昵称和密码')
input_name = input('昵称:')
if not input_name:
    username = generate_username()
    progress_bar(0.1)
    print(f'自动生成昵称: {username}')
else:
    username = check_username(input_name)
print(f'昵称:{username}输入成功')
input_password = input('密码:')
password = check_password(input_password)
input_confirm = input('请再次输入密码:')
confirm_password = check_confirm(input_confirm, password)
print(f'密码:{confirm_password}输入成功')
progress_bar(0.1)
print(f'{username}注册成功！欢迎使用！')