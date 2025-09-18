from calculator import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"{a} + {b} = {add(a,b)}")
    print(f"{a} - {b} = {subtract(a,b)}")
    print(f"{a} * {b} = {multiply(a,b)}")
    print(f"{a} / {b} = {divide(a,b)}")

if __name__ == "__main__":
    main()
