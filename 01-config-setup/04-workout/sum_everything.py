def sum_every(*args):
    total = 0
    for one_number in args:
        total += one_number
    return total

if __name__ == '__main__':
    print(sum_every(5, 3.8, 5))
    print(sum_every(5, 5))
    print(sum_every(10, 20, 30, 40))
