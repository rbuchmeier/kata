def main():
    file = open('input.txt')
    base_line = int(file.readline())
    count = 0
    while True:
        try:
            current_line = int(file.readline())
        except:
            break
        if current_line > base_line:
            count += 1
        base_line = current_line
    print(count)

if __name__ == '__main__':
    main()
