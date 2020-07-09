def cal(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b


if __name__ == '__main__':
    incalstr = input('请输入表达式：')
    callist = []

    strtemp = ''

    for i in incalstr:
        if i in ['/', '+', '-', '*', '(', ')']:
            if strtemp != '':
                callist.append(float(strtemp))
                callist.append(i)
                strtemp = ''
            else:
                callist.append(i)
                strtemp = ''
        else:
            strtemp += i
    print(callist)

    calstrak = []
    if callist[0] == '(':
        calstrak.append('+')

    for i in callist:
        if isinstance(i, float):
            if len(calstrak) > 0:
                if calstrak[-1] == '-':
                    calstrak.pop()
                    calstrak.append('+')
                    calstrak.append(-i)
                elif calstrak[-1] == '/':
                    calstrak.pop()
                    calstrak.append('*')
                    calstrak.append(1 / i)
                elif calstrak[-1] == '*':
                    calstrak.pop()
                    a_2 = calstrak.pop()
                    calstrak.append(a_2 * i)
                else:
                    calstrak.append(i)

            else:
                calstrak.append(i)
        elif i == '-' or i == '+':
            if len(calstrak) > 1:
                if isinstance(calstrak[-1],
                              float) and isinstance(calstrak[-2],
                                                    str) and isinstance(calstrak[-3],
                                                                        float):
                    if calstrak[-2] == '+':
                        a_1 = calstrak.pop()
                        calstrak.pop()
                        a_2 = calstrak.pop()
                        calstrak.append(a_2 + a_1)
                    elif calstrak[-2] == '*':
                        a_1 = calstrak.pop()
                        calstrak.pop()
                        a_2 = calstrak.pop()
                        calstrak.append(a_2 * a_1)
            calstrak.append(i)
        elif i == ')':
            while True:
                if len(calstrak) > 2:
                    if isinstance(calstrak[-1],
                                  float) and isinstance(calstrak[-2],
                                                        str) and isinstance(calstrak[-3],
                                                                            str):
                        if calstrak[-3] == '(' and calstrak[-2] == '+':
                            a1 = calstrak.pop()
                            calstrak.pop()
                            calstrak.pop()
                            if calstrak[-1] == '/':
                                calstrak.pop()
                                calstrak.append('*')
                                calstrak.append(1 / a1)
                            elif calstrak[-1] == '-':
                                calstrak.pop()
                                calstrak.append('+')
                                calstrak.append(-a1)
                            else:
                                calstrak.append(a1)
                            break
                    if isinstance(calstrak[-1],
                                  float) and isinstance(calstrak[-2],
                                                        str) and isinstance(calstrak[-3],
                                                                            float):
                        a_1 = calstrak.pop()
                        op_1 = calstrak.pop()
                        a_2 = calstrak.pop()
                        if op_1 == "+":
                            calstrak.append(a_1 + a_2)
                        if op_1 == "*":
                            calstrak.append(a_1 * a_2)
                if len(calstrak) > 1:
                    if isinstance(calstrak[-2], str):
                        if calstrak[-2] == '(':
                            a1 = calstrak.pop()
                            calstrak.pop()
                            if calstrak[-1] == '-':
                                calstrak.pop()
                                calstrak.append('+')
                                calstrak.append(-a1)

                            elif calstrak[-1] == '/':
                                calstrak.pop()
                                calstrak.append('*')
                                calstrak.append(1 / a1)
                            else:
                                calstrak.append(a1)
                            break

        else:
            calstrak.append(i)
        print(calstrak)
    print(calstrak)

    if calstrak[0] == '+':
        del calstrak[0]
    print(calstrak)
    tmpStrack = []
    while True:
        if len(calstrak) == 0:
            print(sum(tmpStrack))
            break
        a = calstrak.pop()
        if isinstance(a, str):
            if a == '*':
                b = calstrak.pop()
                c = tmpStrack.pop()
                tmpStrack.append(b * c)
            elif a == '+':

                d = calstrak.pop()
                tmpStrack.append(d)
            print(tmpStrack)
        elif isinstance(a, float):
            tmpStrack.append(a)
            print(tmpStrack)
