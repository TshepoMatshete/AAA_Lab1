game = input()
game_visual = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(game[(i * 3) + j])
    game_visual.append(row)

for i in range(3):
    for j in range(3):
        print(game_visual[i][j], end=" ")
    print()