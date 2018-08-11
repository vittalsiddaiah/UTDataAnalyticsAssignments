


def h_line(num = 1, width = 82):
    if num == 1: line = '-'
    if num == 2: line = '='
    full_line =''
    for count in range(width):
        full_line += line
    return full_line
