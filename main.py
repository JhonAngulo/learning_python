user_option = input('piedra, papel o tijera: ')
user_option = user_option.lower()
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('la piedra le gana a la tijera')
        print('Ganaste!')
    else:
        print('el papel le gana a la piedra')
        print('Perdiste!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('el papel le gana a la piedra')
        print('Ganaste!')
    else:
        print('la tijera le gana al papel')
        print('Perdiste!')
else:
    if computer_option == 'papel':
        print('la tijera le gana al papel')
        print('Ganaste!')
    else:
        print('la piedra le gane a  la tijera')
        print('Perdiste!')