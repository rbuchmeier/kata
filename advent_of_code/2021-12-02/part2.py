if __name__ == '__main__':
    distance = 0
    depth = 0
    aim = 0
    with open('input.txt') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            command, value = line.split(' ')

            if command == 'forward':
                distance += int(value)
                depth += aim * int(value)
            elif command == 'down':
                aim += int(value)
            elif command == 'up':
                aim -= int(value)
    print(distance, depth)
    print(distance * depth)
