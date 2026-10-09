def simple_interest(p, r, t):
    return (p * r * t) / 100


def main():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time in years: "))

    result = simple_interest(p, r, t)
    print("Simple Interest =", result)


if __name__ == "__main__":
    main()