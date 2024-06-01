class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

class WrongInputStructureError(Exception):
    pass

def win_or_loose(move1,move2):
    match move1:
        case "R":
            match move2:
                case "R":
                    return 1
                case "P":
                    return 2
                case "S":
                    return 1
                case _:
                    return 0
        case "P":
            match move2:
                case "R":
                    return 1
                case "P":
                    return 1
                case "S":
                    return 2
                case _:
                    return 0
        case "S":
            match move2:
                case "R":
                    return 2
                case "P":
                    return 1
                case "S":
                    return 1
                case _:
                    return 0
        case _:
            return 0

def rps_game_winner(moves : list):
    if len(moves) != 2:
        raise WrongNumberOfPlayersError;

    if len(moves[0]) != 2 or len(moves[1]) != 2:
        raise WrongInputStructureError;

    match win_or_loose(moves[0][1],moves[1][1]):
        case 0:
            raise NoSuchStrategyError
        case 1:
            print(f"{moves[0][0]} {moves[0][1]}")
        case 2:
            print(f"{moves[1][0]} {moves[1][1]}")

# rps_game_winner([['player1','P'],['player2','S'],['player3','S']])
# rps_game_winner([['player1','P'],['player2','A']])
rps_game_winner([['player1','P'],['player2','P']])
rps_game_winner([['player1','R'],['player2','S']])
