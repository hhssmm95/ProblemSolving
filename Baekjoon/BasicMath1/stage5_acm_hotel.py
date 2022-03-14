def solution(row, col, seq):
    front_num = 0
    back_num = 0

    if seq % row != 0:
        back_num = (seq//row) +1
        front_num = seq%row
    else:
        back_num = seq//row
        front_num = row

    if back_num >= 10:
        return f"{front_num}{back_num}"
    else:
        return f"{front_num}0{back_num}"

cases = int(input())

for i in range(cases):
    row, col, seq = map(int, input().split(' '))
    print(solution(row, col, seq))