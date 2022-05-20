def main():
    print("WELCOME TO OUR USELESS STORE!")
    print("*" * 30)
    item = input("What item are you purchasing? ")
    price = float(input(f"What is the price of {item}? "))
    quantity = int(input(f"How many {item}(s) are you buying? "))

    print(f"\n\nAdded {quantity} {item}(s) to shopping cart\nSubtotal: {price*quantity}")

main()