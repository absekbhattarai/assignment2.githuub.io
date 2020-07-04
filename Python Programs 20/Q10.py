def cases(case):
    snake_case = [case[0].lower()]
    snake_case2 = [case[0].lower()]
    for c in case[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            snake_case.append('_')
            snake_case2.append('-')
            snake_case.append(c.lower())
            snake_case2.append(c.lower())
        else:
            snake_case.append(c)
            snake_case2.append(c)

    print(''.join(snake_case))
    print(''.join(snake_case2))
    return "!"


camel_case = input("Enter camel cased sentence: ")
print(cases(camel_case))
