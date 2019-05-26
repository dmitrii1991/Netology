record = input('Введите команду: ')
try:
    operand = record.split(" ")[0]
    number1 = int(record.split(" ")[1])
    number2 = int(record.split(" ")[2])
    print(operand, number1, number2)

    assert  operand  in ["+", "-", "*", "/"], "operator is not indexed"
    if operand == "-":
        rezult = int(number1) - int(number2)
        print("rezult", rezult)
    elif operand == "+":
        rezult = int(number1) + int(number2)
        print("rezult", rezult)
    elif operand == "*":
        rezult = int(number1) * int(number2)
        print("rezult", rezult)
    elif operand == "/":
        rezult = int(number1) / int(number2)
        print("rezult", rezult)

except IndexError:
    print("Command not set correctly")
except ZeroDivisionError:
    print("cannot be divided by 0")
except ValueError:
    print("use integers!")
