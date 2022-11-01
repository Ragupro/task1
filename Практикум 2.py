import os
import shutil as sh


def func1(name, text = None): 
    with open(name, 'w', encoding = 'utf-8') as file:
        if text:
            file.write(text)
    print(f'Файл {name} создан')


def func2(name): 
    print(f'Файл {name} считан')
    with open(name, 'r') as file:
        for line in f:
            print(line)


def func3(name): 
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Эта папка уже создана')
    print(f'Папка {name} создана')


def func4(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)
    print(f'Файл {name} удален')


def func5(name, new_name):
    if os.path.isdir(name):
        try:
            sh.copytree(name, new_name)
        except FileExistsError:
            print('Эта папка уже создана')
    else:
        sh.copy(name, new_name)
    print(f'Файл {name} скопирован с именем {new_name}')


def func6(name, new_name):
    os.rename(name, new_name)
    print(f'Файл {name} переименован на {new_name}')

def func7(name):
    os.chdir(name)
    print('Директория изменена')

def func8():
    pass




if __name__ == '__main__':
    func1('файл.txt')
    func1('файл.txt', 'текст')
    func3('папка')
    func3('папка')
    func4('текст.txt')
    func4('папка')
