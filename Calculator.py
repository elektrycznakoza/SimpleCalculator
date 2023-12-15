import logging

# Configure the root logger once
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="calclogs.log")

def dodawanie(*args):
    return sum(args)

def odejmowanie(a, b):
    return a - b

def mnozenie(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

def dzielenie(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
    return a / b

def main():
    logging.basicConfig(level=logging.INFO)

    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

    operation = int(input())

    if operation not in [1, 2, 3, 4]:
        print("Nieprawidłowa operacja.")
        return

    args = []
    if operation in [1, 3]:
        print("Podaj składniki oddzielone spacją:")
        args = list(map(float, input().split()))
    else:
        print("Podaj składnik 1:")
        args.append(float(input()))
        print("Podaj składnik 2:")
        args.append(float(input()))

    operation_name = {
        1: "Dodawanie",
        2: "Odejmowanie",
        3: "Mnożenie",
        4: "Dzielenie"
    }[operation]

    logging.info(f"{operation_name} {', '.join(map(str, args))}")   

    result = None
    if operation == 1:
        result = dodawanie(*args)
    elif operation == 2:
        result = odejmowanie(*args)
    elif operation == 3:
        result = mnozenie(*args)
    elif operation == 4:
        try:
            result = dzielenie(*args)
        except ValueError as error:
            print(error)
            return

    print(f"{operation_name} {', '.join(map(str, args))}")
    print(f"Wynik to {result:.2f}")

if __name__ == "__main__":
    main()
