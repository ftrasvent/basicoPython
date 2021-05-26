import random

def password_generator():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    characters = mayus + minus + symbols + nums

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)
    
    password = "".join(password)
    return password

def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()