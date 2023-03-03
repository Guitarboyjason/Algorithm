import sys
sys.stdin = open("sources/input-6.txt", "r")


def is_it_okay(sudoku):
    for i in range(9):
        row = []
        column = []
        for j in range(9):
            row.append(sudoku[i][j])
            column.append(sudoku[j][i])
        if len(set(row)) != 9 or len(set(column)) != 9:
            return 0

    for i in range(3):
        for j in range(3):
            arr = []
            for k in range(3):
                for l in range(3):
                    arr.append(sudoku[3*i+k][3*j+l])
            if len(set(arr)) != 9:
                return 0
    return 1


T = int(input())
for test_case in range(1, T+1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    print("#{} {}".format(test_case, is_it_okay(sudoku)))
