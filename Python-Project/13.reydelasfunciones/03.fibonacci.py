def fibonacci(position):
    sequence_fibonacci = [0, 1]
    if position == 0:
        return "0"
    if position == 1:
        return "0, 1"

    for el in range(2, position + 1):
       num = sequence_fibonacci[el - 2] + sequence_fibonacci[el - 1]
       sequence_fibonacci.append(num)

    return ", ".join(str(el) for el in sequence_fibonacci)

def fibonacci_recursiva(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1

    return fibonacci_recursiva(position - 1) + fibonacci_recursiva(position - 2)

def power_number(base, power = 2):
    return base ** power

if __name__ == "__main__":
    print(fibonacci(8))
    print(fibonacci_recursiva(3))
    print(power_number(3, 9))