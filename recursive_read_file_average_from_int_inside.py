"""
- Task 1
# average(filename) ascii
# integers one per line

## return average of intergers

- Task 2
# now besides integers, filenames can apper,
## and the program consider the integers inside `n` files
## returns average of all intergers

"""


def average_from_files(fname: str) -> float:
    def read_int_from_files(filename: str) -> list:
        average: list = []
        with open(filename) as f:
            for line in f:
                try:
                    average.append(int(line))
                except ValueError:
                    average.extend(read_int_from_files(line.rstrip('\n')))

        return average
    numbers = read_int_from_files(fname)
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    print(average_from_files('start.txt'))


