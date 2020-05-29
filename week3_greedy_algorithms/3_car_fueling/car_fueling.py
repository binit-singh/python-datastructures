# python3


def compute_min_refills(distance, tank, stops):
    # write your code here
    fill_up = 0
    current_pos = 0
    stops_count = len(stops)
    stops.insert(0, 0)
    stops.append(distance)
    while current_pos <= stops_count:
        last_refill = current_pos
        while current_pos <= stops_count and stops[current_pos+1] - stops[last_refill] <= tank:
            current_pos += 1
        if current_pos == last_refill:
            return -1
        if current_pos <= stops_count:
            fill_up += 1

    return fill_up


if __name__ == '__main__':
    distance = int(input())
    tank = int(input())
    stops_count = input()
    stops = list(map(int, input().split()))
    print(compute_min_refills(distance, tank, stops))
