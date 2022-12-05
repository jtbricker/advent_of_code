from lib.helpers import load_input


PAIRS = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>',
}


def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [d.strip() for d in data]

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    SCORES = {
        ')':3,
        '}':1197,
        ']':57,
        '>':25137,
    }

    illegal_characters = []
    for line in data:
        # print("line", line)
        running = []
        if line[0] not in PAIRS.keys():
            illegal_characters.append([0])
            continue
        for c in line:
            if c in PAIRS.keys():
                running.append(c)
            else:
                last_running_char = running[-1]
                if c == PAIRS[last_running_char]:
                    running.pop()
                else:
                    # print(f"Found illegal character: {c}")
                    illegal_characters.append(c)
                    break
            # print("running", running)

    return sum([SCORES[c] for c in illegal_characters])

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    incomplete_chunks = []
    for line in data:
        # print("line", line)
        corrupt = False
        running = []
        if line[0] not in PAIRS.keys():
            corrupt = True
            continue
        for c in line:
            if c in PAIRS.keys():
                running.append(c)
            else:
                last_running_char = running[-1]
                if c == PAIRS[last_running_char]:
                    running.pop()
                else:
                    # print(f"Found illegal character: {c}")
                    corrupt = True
                    break
            # print("running", running)
        if len(running) != 0 and not corrupt:
            incomplete_chunks.append(running)

    scores = [calculate_score(chunk) for chunk in incomplete_chunks]


    return sorted(scores)[len(scores)//2]

def calculate_score(chunk):
    SCORES = {
        ')':1,
        '}':3,
        ']':2,
        '>':4,
    }

    completion_string = [PAIRS[c] for c in chunk[::-1]]
    print("".join(completion_string))
    score = 0
    for s in completion_string:
        score = 5*score + SCORES[s]

    return score

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()