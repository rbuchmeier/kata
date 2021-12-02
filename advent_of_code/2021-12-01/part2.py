def main():
    count = 0
    lines = []
    with open('input.txt') as f:
        lines.append(int(f.readline()))
        lines.append(int(f.readline()))
        lines.append(int(f.readline()))
        while True:
            current_sum = sum(lines)
            lines.pop(0)
            try:
                lines.append(int(f.readline()))
            except:
                break
            next_sum = sum(lines)
            if next_sum > current_sum:
                count += 1
    return count

if __name__ == '__main__':
    print(main())
