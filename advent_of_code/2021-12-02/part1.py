if __name__ == "__main__":
    distance = 0
    depth = 0
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            command, num = line.strip().split(' ')
            if command == "forward":
                distance += int(num)
            elif command == "up":
                depth -= int(num)
            elif command == "down":
                depth += int(num)
    print(distance, depth)
    print(distance * depth)
