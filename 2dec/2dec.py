from math import prod

with open("2dec/in2.txt") as file:
    available = {"red": 12, "green": 13, "blue": 14}
    possible_games = []
    power = 0

    for line in file:
        gameId, cubes = line.strip().split(":")
        gameId = int(gameId.split()[1])
        cubes = cubes.split(";")
        possible = True
        dict = {"red": 0, "green": 0, "blue": 0}
        
        for subset in cubes:
            subset = subset.split(",")
            for pair in subset:
                for part in pair.split():
                    if part.isdigit():
                        amount = int(part)
                    else:
                        color = part
                if available[part] < amount:
                    possible = False
                dict[part] = max(dict[part], amount)
        if possible:
            possible_games.append(gameId)
        
        power += prod(dict.values())

    print(sum(possible_games))
    print(power)