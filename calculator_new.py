status = True
stop = False
while status or stop:  # if while loop is true running the program every time when be while loop is false stop the
    # program

    while True:  # if while loop is true running the program every time when be while loop is false stop the program

        try:  # this is to fix the error

            number_1 = float(input("Please enter the first number:==> "))  # get input numeric values from user
            break  # this line to stop loop when be false

        except ValueError:  # print type of error at Windows user
            print("Please enter type of numeric value ")
    while True:  # if while loop is true running the program every time when be while loop is false stop the program
        try:
            operator = input("Please enter type of operator:==> ")  # get input operator from user
            if operator in ["+", "-", "*", "/", "%", "//", "=", "<", ">", "^", "<=", ">=", "!="]:
                break
            else:
                raise ValueError
        except ValueError:
            print("the operator is wrong please enter type of operator (+,-*,/,%,//,=,<,>,^,<,=,>=,!=)")
    while True:  # if while loop is true running the program every time when be while loop is false stop the program

        try:  # this is to fix the error

            number_2 = float(input("Please enter the second number:==> "))  # get input numeric values from user
            if operator == "/" and number_2 == 0:  # conditions statements when user enter division by zero
                raise ZeroDivisionError
            break  # this line to stop loop when be false

        except ValueError:  # print type of error
            print("Please enter the type of numeric value ")
        except ZeroDivisionError:
            print("(this is zero division error)can not divided by zero, Please enter the another numeric value")

    if operator == "-":  # condition statements number  subtraction number
        print(number_1 - number_2)

    elif operator == "+":  # condition statements number addition number
        print(number_1 + number_2)

    elif operator == "/":  # condition statements number division number
        print(number_1 / number_2)

    elif operator == "*":  # condition statements number multiplication number
        print(number_1 * number_2)

    elif operator == "%":  # condition statements number modulus number
        print(number_1 % number_2)

    elif operator == "//":  # conditional statements number floor division number
        print(number_1 // number_2)

    elif operator == "^":  # conditional statements  number	exponentiation  number
        print(number_1 ** number_2)

    elif operator == ">":  # conditional statements number greater than number
        if number_1 > number_2:
            print(number_1, " greater than ", number_2)
            print(number_1 >= number_2)

        elif number_2 > number_1:
            print(number_2, " greater than ", number_1)
            print(number_2 >= number_1)

        elif number_1 == number_2:
            print(number_1, " equal ", number_2)
            print(number_1 == number_2)

    elif operator == "<":  # condition statements number less than number
        if number_1 < number_2:
            print(number_1, " less than ", number_2)
            print(number_1 < number_2)

        elif number_2 < number_1:
            print(number_2, " less than ", number_1)
            print(number_2 < number_1)

        elif number_1 == number_2:
            print(number_1, " equal ", number_2)
            print(number_1 == number_2)

    elif operator == ">=":  # condition statements number greater than  or equal to  number
        if number_1 > number_2:
            print(number_1, " greater than ", number_2)
            print(number_1 >= number_2)

        elif number_2 > number_1:
            print(number_2, " greater than ", number_1)
            print(number_2 >= number_1)

        elif number_1 == number_2:
            print(number_1, " equal ", number_2)
            print(number_1 == number_2)

    elif operator == "<=":  # condition statements number less than or equal to number
        if number_1 < number_2:
            print(number_1, " less than ", number_2)
            print(number_1 <= number_2)

        elif number_2 < number_1:
            print(number_2, " less than ", number_1)
            print(number_2 <= number_1)

        elif number_1 == number_2:
            print(number_1, " equal ", number_2)
            print(number_1 == number_2)

    elif operator == "=":  # condition statements number equal number
        if number_1 == number_2:
            print(number_1, " equal ", number_2)
            print(number_1 == number_2)

        elif number_2 == number_1:
            print(number_2, " equal ", number_1)
            print(number_2 == number_1)

        elif number_1 != number_2:  # condition statements number not equal number
            print(number_1, "not equal ", number_2)
            print(number_1 != number_2)

        elif number_2 != number_1:
            print(number_2, " not equal ", number_1)
            print(number_2 != number_1)

            # else:
    # print("the operator is wrong please enter type of operator (+,*,/,=,%,-,>,< <=,>=,=,)")

    while status or stop:  # if while loop is true running the program every time when be while loop is false stop
        # the program
        try:
            repeat = str(input("do you want perform  another calculation (continue/stop)==> "))
            if repeat == "continue":
                status = True
                print("the program is continue")
                break
            elif repeat == "stop":
                status = False
                print("the program is break")
            else:
                raise ValueError
        except ValueError:
            print( "word incorrect if you want perform another calculation enter (continue) or do want to exit enter "
                   "(stop)==> ")

print("program exited")
