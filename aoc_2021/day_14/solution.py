from lib.helpers import load_input
import collections
from functools import lru_cache

cache = {}

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    template = data[0]
    mapping = {}
    for d in data[1:]:
        parts = [x.strip()  for x in d.split('->')]
        mapping[parts[0]] = parts[1]
    
    return template, mapping

def step(template, mapping):
    new_template = ""
    for i in range(0,len(template)-1):
        pair = template[i:i+2]
        insert = mapping[pair]
        new_template += pair[0] + insert
        i += 1
    new_template += template[-1]
    return new_template


class Polymer:
    def __init__(self, mapping):
        self.mapping = mapping

    def transcribe(self, template):
        global cache
        if template in cache:
            return cache[template]
        else:
            length = len(template)
        if length == 2:
            res = template[0] + self.mapping[template] + template[1]
            cache[template] = res
            return res
        
        else:
            p1 = template[:length//2+1]
            p2 = template[length//2:]
            res1 = self.transcribe(p1)
            res2 = self.transcribe(p2)
            result = res1[:-1] + res2
            cache[template] = result
            return result



def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    template, mapping = parse_data(data)

    poly = Polymer(mapping)

    for i in range(10):
        template = poly.transcribe(template)

    most_to_least = collections.Counter(template).most_common()

    res =  most_to_least[0][1] - most_to_least[-1][1]
    print(res)
    return res

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    template, mapping = parse_data(data)
    
    initial_pairs = []
    for i in range(len(template)-1):
        initial_pairs.append(template[i:i+2])
    element_counts = {}
    for i in range(len(template)):
        elem = template[i]
        cur_count = element_counts.get(elem,0)
        element_counts[elem] = cur_count + 1

    poly = Polymer(mapping)
    counts = {k:1 for k in initial_pairs}
    for i in range(40):
        new_counts = {}
        for pair, count in counts.items():
            p = poly.transcribe(pair)
            p1 = p[0:2]
            p2 = p[1:]

            cur_count = element_counts.get(p[1],0)
            element_counts[p[1]] = cur_count + count
            
            p1_count = new_counts.get(p1,0)
            p2_count = new_counts.get(p2,0)

            new_counts[p1] = count + p1_count
            new_counts[p2] = count + p2_count
        counts = new_counts.copy()
    
    return max(element_counts.values()) - min(element_counts.values())

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()