game = input()

posible_moves = []

curr_pos = game.find("#")

if curr_pos - 3 >= 0:
    posible_moves.append("UP")

if curr_pos + 3 < len(game):
    posible_moves.append("DOWN")

if curr_pos - 1 >= 0:
    posible_moves.append("LEFT")

if curr_pos + 1 < len(game):
    posible_moves.append("RIGHT")

for move in posible_moves:
    print(move)