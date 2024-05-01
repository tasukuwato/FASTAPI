price = 100
tax = 1.1

def calc_price_include_tax(price, tax):
    return int(price*tax)

if __name__ == "__main__":
    print(f"{calc_price_include_tax(price=price, tax = tax)}円")
