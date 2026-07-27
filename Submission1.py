game = input()
move = input()

curr_pos = game.find("#")
game = list(game)


if move == "LEFT" and curr_pos > 0:
    temp_pos = curr_pos - 1
    game[curr_pos], game[temp_pos] = game[temp_pos], game[curr_pos]

elif move == "RIGHT" and curr_pos < len(game) - 1:
    temp_pos = curr_pos + 1
    game[curr_pos], game[temp_pos] = game[temp_pos], game[curr_pos]
   
elif move == "UP" :
     temp_pos = curr_pos - 3
     game[curr_pos], game[temp_pos] = game[temp_pos], game[curr_pos]

elif move == "DOWN" :
     temp_pos = curr_pos + 3
     game[curr_pos], game[temp_pos] = game[temp_pos], game[curr_pos]

game = ''.join(game)
print(f"The positions of # was in {curr_pos}. The new game state is {game}")