from lib.helpers import load_input

class Something:
    def __init__(self):
        pass
    
class CubeSet:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    @classmethod
    def from_raw_set_str(cls, raw_set_str):
        set_parts = [x.strip() for x in raw_set_str.strip().split(',')]
        _set = {}
        for sp in set_parts:
            x = sp.split(' ')
            _set[x[1]] = int(x[0])
        red = _set.get('red', 0)
        green = _set.get('green', 0)
        blue = _set.get('blue', 0)

        return cls(red, green, blue)

    @property
    def power(self):
        return self.red * self.green * self.blue
    
    def __str__(self):
        return f"R:{self.red}, G:{self.green}, B:{self.blue}"
    
    def __repr__(self):
        return f"CubeSet({self.red}, {self.green}, {self.blue})"

class Game:
    def __init__(self, game_id, cube_sets):
        self.game_id = game_id
        self.cube_sets = cube_sets

    @classmethod
    def from_raw_game_str(cls, raw_game_str):
        game_str, sets_str = raw_game_str.split(":")
        game_id = int(game_str.split()[1])

        sets_raw = sets_str.split(';')
        cube_sets = [CubeSet.from_raw_set_str(s) for s in sets_raw]

        return cls(game_id, cube_sets)

    @property
    def max_red(self):
        return max([s.red for s in self.cube_sets])

    @property
    def max_green(self):
        return max([s.green for s in self.cube_sets])

    @property
    def max_blue(self):
        return max([s.blue for s in self.cube_sets])

    def is_game_possible(self, total_red, total_green, total_blue):
        return total_red >= self.max_red and total_green >= self.max_green and total_blue >= self.max_blue
    
    @property
    def smallest_possible_total_cube_set(self):
        return CubeSet(self.max_red, self.max_green, self.max_blue)

    def __str__(self):
        return f"Game {self.game_id} has {len(self.cube_sets)} sets: {[str(s) for s in self.cube_sets]}"

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [Game.from_raw_game_str(d) for d in data]

def part_1(data):
    """ For a list of games, determine if the game is possible under the required conditions 
    and return the sum of the game ids that are possible

    In the game, a bag of red, green, and blue cubes are given to the player, who draws multiple sets of cubes at random and records the number of each color drawn.

    The game is "possible" if the total red, green, and blue cubes in all of the sets is less than or equal to the total red, green, and blue cubes available in the bag.

    There are 12 red, 13 green, and 14 blue cubes available

    Args:
        data (list(str)): List of game strings of the format "Game #ID: #RED red, #GREEN green, #BLUE blue; #RED red, #GREEN green, #BLUE blue; ..."

    Returns:
        int: Sum of game ids that are possible
    """
    games = parse_data(data)

    TOTAL_RED = 12
    TOTAL_GREEN = 13
    TOTAL_BLUE = 14

    total = 0
    for game in games:
        if game.is_game_possible(TOTAL_RED, TOTAL_GREEN, TOTAL_BLUE):
            total += game.game_id
    return total

def part_2(data):
    """ For a list of games, determine the "power" of the smallest possible cube set for each game
    and return the sum of the powers for all games.

    In the game, a bag of red, green, and blue cubes are given to the player, who draws multiple sets of cubes at random and records the number of each color drawn.

    The game is "possible" if the total red, green, and blue cubes in all of the sets is less than or equal to the total red, green, and blue cubes available in the bag.

    The "power" of a cube set is the product of the red, green, and blue cubes in the set.

    Args:
        data (list(str)): List of game strings of the format "Game #ID: #RED red, #GREEN green, #BLUE blue; #RED red, #GREEN green, #BLUE blue; ..."

    Returns:
        int: Sum of game ids that are possible
    """
    games = parse_data(data)

    total = 0
    for game in games:
        total += game.smallest_possible_total_cube_set.power
    return total

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()
