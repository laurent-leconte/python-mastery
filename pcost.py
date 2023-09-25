def portfolio_cost(filename):
    total = 0.0
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            _, quant, price, *rest = line.split()
            try:
                total += int(quant) * float(price)
            except ValueError as e:
                print("Couldn't parse:", line)
                print("Reason:", e)

    return total

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))