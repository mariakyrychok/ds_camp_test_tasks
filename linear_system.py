import numpy as np


def parse_row(raw_input):
    return np.array(list(map(int, raw_input.split())))


def main():
    rows, columns = 3, 3
    matrix_a = []

    print("Enter three entries of the row separated by space, and use enter to start a new row: ")
    for i in range(rows):
        single_row = parse_row(input())
        if len(single_row) == columns:
            matrix_a.append(single_row)
        else:
            raise TypeError("Please enter three entries separated by space")

    print("Enter three entries of vector B separated by space: ")
    vector_b = parse_row(input())
    try:
        solution_x = np.linalg.solve(matrix_a, vector_b)
        print("The solution: ", np.round(solution_x, 2))
    except np.linalg.LinAlgError:
        print("The solution does not exist")


if __name__ == '__main__':
    main()
