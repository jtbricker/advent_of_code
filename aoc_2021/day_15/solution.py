import numpy as np

from lib.helpers import load_input

nodes = {}
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())


def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [[int(x) for x in row] for row in data]

class Node:
    def __init__(self, x, y, weight, m, n):
        self.x = x
        self.y = y
        self.weight = weight
        self.max_x = m
        self.max_y = n

    def get_valid_neighbors(self, visited):
        m = self.max_x
        n = self.max_y
        i = self.x
        j = self.y
        
        adjacent_indices = []
        if i > 0:
            adjacent_indices.append((i-1,j))
        if i+1 < m:
            adjacent_indices.append((i+1,j))
        if j > 0:
            adjacent_indices.append((i,j-1))
        if j+1 < n:
            adjacent_indices.append((i,j+1))
        
        return [nodes[p] for p in adjacent_indices if p not in visited]

    @property
    def point(self):
        return (self.x, self.y)

cache = {}

def find_min_risk_path(start, end, visited):
    print(f"find_min_risk_path({start}, {end}, {visited})")
    if cache.get(start):
        return cache.get(start)

    current = nodes[start]
    end_point = nodes[end]
    new_visited = visited.copy() + [start]

    # import pudb; pudb.set_trace()
    neighbors = current.get_valid_neighbors(visited)
    
    if end_point in neighbors:
        res = current.weight + end_point.weight
        print(f"Found endpoint at {current.point}: ", res)
    
    elif len(neighbors) == 0:
        # deadend
        return float("inf")
    
    else:
        res = current.weight + min([find_min_risk_path(p.point, end, new_visited) for p in neighbors])
        print(f"Min from {current.point}: ", res)
    
    cache[start] = res
    return res


def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data =  np.array([[int(y) for y in list(x)] for x in parse_data(data)])
    m = len(data)
    n = len(data[0])

    for i in range(m):
        for j in range(n):
            weight = 0 if (i == 0 and j ==0) else data[i][j]
            nodes[(i,j)] = Node(i,j, weight, m, n)

    starting_point = (0,0)
    end_point = (m-1,n-1)
    risk = find_min_risk_path(starting_point, end_point, [])

    return risk
    
def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    return "Part 2 Not Implemented"

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()