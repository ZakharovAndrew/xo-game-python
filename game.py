# Крестики-нолики на Python (ver. 0.1)
# --------------------------------
# Автор: Захаров Андрей (https://github.com/ZakharovAndrew)
# Ютуб-канал: https://www.youtube.com/@user-sy8gi9gn6v

# размер в клетках для игрового поля
board_size = 3
# игровое поле
board = [1,2,3,4,5,6,7,8,9]


def draw_board():
	''' Выводим игровое поле '''
	print (('_' * 4 * board_size ))
	for i in range(board_size):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

def check_win():
	''' Проверяем победу одного из игроков '''
	win = False

	win_combination = (
		(0,1,2), (3,4,5), (6,7,8),	# горизонтальные линии
		(0,3,6), (1,4,7), (2,5,8),	# вертикальные линии
		(0,4,8), (2,4,6) 			# диагональные линии
	)

	for pos in win_combination:
		# если три ячейки совпадает
		# для урока покажу вариант ниже
		# len(set([board[pos[0]], board[pos[1]], board[pos[2]]]))
		if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
			win = board[pos[0]]

	return win

def game_step(index, char):
	''' Функция хода игрока '''
	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False

	board[index-1] = char
	return True

def start_game():
	# текущий игрок
	current_player = 'X'
	# номер шага
	step = 1

	draw_board()

	# игра продолжается до тех пор, пока кто-то не выиграет или выйдет
	while (step < 9) and (check_win() == False):
		index = input('Ходит ' + current_player + '. Введите номер поля (0 - выход):')

		if (int(index) == 0):
			break

		# если получилось сделать шаг
		if (game_step(int(index), current_player)):
			print('Удачный ход')

			if (current_player == 'X'):
				current_player = 'O'
			else:
				current_player = 'X'

			draw_board()
			# увеличим номер шага
			step += 1
		else:
			print('Неверный номер! Повторите!')

	if (step == 9):
		print('Игра оконцена. Ничья!')
	else:
		print('Выиграл ' + check_win())

print('Добро пожаловать в игру!')
start_game()
