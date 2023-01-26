def arithmetic_arranger(arr, status=False):
    first = ''
    second = ''
    third = ''
    fourth = ''
    if len(arr) > 5:
        return "Error: Too many problems."
    for i in range(len(arr)):
        operand1, operation, operand2 = arr[i].split(" ")
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
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
    print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'], True))


if __name__ == '__main__':
    main()
