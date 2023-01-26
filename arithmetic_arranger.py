def arithmetic_arranger(arr, status):
    first = ''
    second = ''
    third = ''
    fourth = ''
    for i in range(len(arr)):
        operand1, operation, operand2 = arr[i].split(" ")
        o1 = 0
        o2 = 0
        try:
            o1 = int(operand1)
            o2 = int(operand2)
        except:
            return "Error: Numbers must only contain digits."

        m = len(operand1)
        if len(operand1) < len(operand2):
            m = len(operand2)
        first += '{num:>{width}}'.format(num=operand1, width=m + 2)
        second += operation + ' {num:>{width}}'.format(num=operand2, fill='0', width=m)
        third += '{num:-<{width}}'.format(num='-', width=m + 2)
        res = 0
        if operation == "+":
            res = int(operand1) + int(operand2)
        elif operation == "-":
            res = int(operand1) - int(operand2)
        else:
            return "Error: Operator must be '+' or '-'."
        fourth += '{num:>{width}}'.format(num=res, width=m + 2)
        if i != len(arr) - 1:
            first += '    '
            second += '    '
            third += '    '
            fourth += '    '
    if status:
        return first + "\n" + second + "\n" + third + "\n" + fourth
    else:
        return first + "\n" + second + "\n" + third


def main():
    arr = []
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))


if __name__ == '__main__':
    main()
