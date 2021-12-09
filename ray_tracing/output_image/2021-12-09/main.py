import sys

def output_image_to_file(filename):
    columns = 255
    rows = 255
    toolbar_width = 100
    setup_toolbar(toolbar_width - 1)
    current_percentage = 0
    with open(filename, 'w') as f:
        f.write('P3\n')
        f.write(f'{columns} {rows}\n')
        f.write('255\n')
        for i in range(columns):
            if i / columns > current_percentage:
                current_percentage += 0.01
                write_to_progress_bar()
            for j in range(rows):
                f.write(f'{i} {rows - j} 100\n')
    sys.stdout.write('\n')

def write_to_progress_bar():
    sys.stdout.write('=')
    sys.stdout.flush()

def setup_toolbar(width):
    sys.stdout.write(f'[{width * " "}]')
    sys.stdout.flush()
    sys.stdout.write("\b" * (width+1)) # return to start of line, after '['
        
if __name__ == '__main__':
    output_image_to_file('output.ppm')