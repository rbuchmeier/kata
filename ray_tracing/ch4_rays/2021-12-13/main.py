import sys

FILENAME = 'background.ppm'
WIDTH = 1600
HEIGHT = 900

def color_text(r, g, b):
    return f'{r} {g} {b}\n'

def convert_percent_to_rgb(percent):
    return int(percent * 255)

def add_progress():
    sys.stdout.write(f'=')
    sys.stdout.flush()

def write_header(file):
    file.write('P3\n')
    file.write(f'{WIDTH} {HEIGHT}\n')
    file.write('255\n')

def write_progress_bar():
    sys.stdout.write(f'[{100 * " "}')
    sys.stdout.flush()
    sys.stdout.write('\b' * 101)

def main():
    with open(FILENAME, 'w') as file:
        write_header(file)
        write_progress_bar()
        percent_complete = 0

        for y in range(HEIGHT):
            percent_non_blue = (1 - y / HEIGHT) * 0.6 + y / HEIGHT * .9
            r = convert_percent_to_rgb(percent_non_blue)
            g = convert_percent_to_rgb(percent_non_blue)
            b = 255

            file.write(color_text(r, g, b) * WIDTH)

            if y / HEIGHT > percent_complete:
                percent_complete += 0.01
                add_progress()

if __name__ == '__main__':
    main()
