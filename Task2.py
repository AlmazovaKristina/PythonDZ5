import random

s = random.randint(0, 1)
print(s)
cell = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'{cell[0]} | {cell[1]} | {cell[2]} | ')
print('-----------')
print(f'{cell[3]} | {cell[4]} | {cell[5]} | ')
print('-----------')
print(f'{cell[6]} | {cell[7]} | {cell[8]} |  ')

if s == 0:
    h = 'игрок'
else:
    h = 'компьютер'
for i in range(len(cell)):
    while cell[i] != 'X' and cell[i] != 'O':
        if s == 0:
            turn = int(input('Куда хотите сходить? '))
            if cell[turn - 1] == 'X' or cell[turn - 1] == 'O':
                print(f'Ячейка {turn} уже занята')
                print(h)
            else:
                cell[turn - 1] = 'X'
                s = 1
            print(f'{cell[0]} | {cell[1]} | {cell[2]} | ')
            print('-----------')
            print(f'{cell[3]} | {cell[4]} | {cell[5]} | ')
            print('-----------')
            print(f'{cell[6]} | {cell[7]} | {cell[8]} |  ')
            print('-----------------------------------------')
        else:
            j = random.randint(1, 9)
            print(f'Компьютер сходил {j}')
            if cell[j - 1] == 'X' or cell[j - 1] == 'O':
                print(f'Ячейка {j} уже занята')
                print(h)
            else:
                cell[j - 1] = 'O'
                s = 0
            print(f'{cell[0]} | {cell[1]} | {cell[2]} | ')
            print('-----------')
            print(f'{cell[3]} | {cell[4]} | {cell[5]} | ')
            print('-----------')
            print(f'{cell[6]} | {cell[7]} | {cell[8]} |  ')
            print('-----------------------------------------')
        if cell[0] == 'X' and cell[1] == 'X' and cell[2] == 'X' or cell[0] == 'O' and cell[1] == 'O' and cell[
            2] == 'O':
            print(f'Победил {h}')
            break
        elif cell[3] == 'X' and cell[4] == 'X' and cell[5] == 'X' or cell[3] == 'O' and cell[4] == 'O' and cell[
            5] == 'O':
            print(f'Победил {h}')
            break
        elif cell[6] == 'X' and cell[7] == 'X' and cell[8] == 'X' or cell[6] == 'O' and cell[7] == 'O' and cell[
            8] == 'O':
            print(f'Победил {h}')
            break
        elif cell[0] == 'X' and cell[3] == 'X' and cell[6] == 'X' or cell[0] == 'O' and cell[3] == 'O' and cell[
            6] == 'O':
            print(f'Победил {h}')
            break
        elif cell[1] == 'X' and cell[4] == 'X' and cell[5] == 'X' or cell[1] == 'O' and cell[4] == 'O' and cell[
            5] == 'O':
            print(f'Победил {h}')
            break
        elif cell[2] == 'X' and cell[5] == 'X' and cell[8] == 'X' or cell[2] == 'O' and cell[5] == 'O' and cell[
            8] == 'O':
            print(f'Победил {h}')
            break
        elif cell[0] == 'X' and cell[4] == 'X' and cell[8] == 'X' or cell[0] == 'O' and cell[4] == 'O' and cell[
            8] == 'O':
            print(f'Победил {h}')
            break
        elif cell[2] == 'X' and cell[4] == 'X' and cell[6] == 'X' or cell[2] == 'O' and cell[4] == 'O' and cell[
            6] == 'O':
            print(f'Победил {h}')
        break
