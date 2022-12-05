from lib.helpers import load_input

class BoardingPass:

    def __init__(self, boarding_pass_str):
        self.row = self._get_row_number(boarding_pass_str[:7])
        self.seat = self._get_seat_number(boarding_pass_str[7:])
        self.seat_id = self.row * 8 + self.seat
    
    def _get_row_number(self, row_str):
        """Get row number from row string.  Row string contains either 'F' or 'B',
        indicating whether the row belongs in either the "F"ront or "B"ack half
        of subsequent halfs of a 128 row plane (indexed 0, rows 0 - 127)

        Args:
            row_str (str): binary space partition str (string containing 'F' and 'B')

        Returns:
            int: row number (between 0 and 127)
        """
        return self._binary_partition(row_str, num_partitions=128, first_half_character='F')

    def _get_seat_number(self, seat_str):
        """Get seat number from seat string.  Seat string contains either 'L' or 'R',
        indicating whether the seat belongs in either the "L"eft or "R"ight half
        of subsequent halfs of a 6 seat row (indexed 0, seats 0 - 7s)

        Args:
            seat_str (str): binary space partition str (string containing 'L' and 'R')

        Returns:
            int: seat number (between 0 and 7)
        """
        return self._binary_partition(seat_str, num_partitions=8, first_half_character='L')

    def _binary_partition(self, partition_str, num_partitions, first_half_character):
        parts = list(range(num_partitions))
        for c in partition_str:
            half = int(len(parts)/2)
            if c == first_half_character:
                parts = parts[0:half]
            else:
                parts = parts[half:]
        return parts[0]

def part_1(data):
    """Find the maximum boarding pass id from the boarding passes 

    Args:
        data (List[BoardingPass]): List of Boarding Passes
    """
    return max([p.seat_id for p in data])

def part_2(data):
    """Find the missing seat id from boarding passes, where the adjacent seats (seat_id +- 1) are present

    Args:
        data (List[BoardingPass]): List of Boarding Passes
    """
    ids = [p.seat_id for p in data]
    for i in range(127 * 8 + 7 + 1):
        if i not in ids and (i - 1) in ids and (i + 1) in ids:
            return i

def main():
    data = [BoardingPass(p) for p in load_input(__file__)]

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()