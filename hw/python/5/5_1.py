import random
def making_card_list() -> list:
	card_list = []
	for shape in ["spade", "heart", "diamond", "clover"]:
		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
			card_list.append((shape, number))
	return card_list

def change_card_list():
	if player1[0] == 4:
		player1[0] = 'spade'
	elif player1[0] == 3:
		player1[0] = 'diamond'
	elif player1[0] == 2:
		player1[0] = 'heart'
	elif player1[0] == 1:
		player1[0] = 'clover'
	if player1[1] == 11:
		player1[1] = 'J'
	elif player1[1] == 12:
		player1[1] = 'Q'
	elif player1[1] == 13:
		player1[1] = 'K'
	elif player1[1] == 14:
		player1[1] = 'A'
	if player2[0] == 4:
		player2[0] = 'spade'
	elif player2[0] == 3:
		player2[0] = 'diamond'
	elif player2[0] == 2:
		player2[0] = 'heart'
	elif player2[0] == 1:
		player2[0] = 'clover'
	if player2[1] == 11:
		player2[1] = 'J'
	elif player2[1] == 12:
		player2[1] = 'Q'
	elif player2[1] == 13:
		player2[1] = 'K'
	elif player2[1] == 14:
		player2[1] = 'A'

trump_card_list = making_card_list()
for i in range(len(trump_card_list)):
	trump_card_list[i] = list(trump_card_list[i])
	if trump_card_list[i][0] == 'spade':
		trump_card_list[i][0] = 4
	elif trump_card_list[i][0] == 'diamond':
		trump_card_list[i][0] = 3
	elif trump_card_list[i][0] == 'heart':
		trump_card_list[i][0] = 2
	elif trump_card_list[i][0] == 'clover':
		trump_card_list[i][0] = 1
	if trump_card_list[i][1] == 'J':
		trump_card_list[i][1] = 11
	elif trump_card_list[i][1] == 'Q':
		trump_card_list[i][1] = 12
	elif trump_card_list[i][1] == 'K':
		trump_card_list[i][1] = 13
	elif trump_card_list[i][1] == 'A':
		trump_card_list[i][1] = 14
trump_card_list.sort(key=lambda x:x[0], reverse=True)
trump_card_list.sort(key=lambda x:x[1], reverse=True)
p1_score = p2_score = 0
while p1_score < 6 and p2_score < 6:
	player1 = random.choice(trump_card_list)
	player2 = random.choice(trump_card_list)
	if trump_card_list.index(player1) < trump_card_list.index(player2):
		change_card_list()
		print(f'({player1[0]}, {player1[1]}) ({player2[0]}, {player2[1]}) player1 win!')
		p1_score+=1
	else :
		change_card_list()
		print(f'({player1[0]}, {player1[1]}) ({player2[0]}, {player2[1]}) player2 win!')
		p2_score+=1
if p1_score == 6:
	print(f'{p1_score}:{p2_score} Finally player1 win')
else :
	print(f'{p1_score}:{p2_score} Finally player2 win')