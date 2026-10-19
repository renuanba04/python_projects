from art import logo
print(logo)

bids = {}
pending_bidders = "yes"
while pending_bidders == "yes":
    # Ask the user for input
    name = input("What is your name?:  ").strip()
    price = int(input("What is your bid?: $").strip())

    # Save data into dictionary {name: price}
    bids[name] = price

    # Whether if new bids need to be added
    pending_bidders = input("Are there any other bidders? Type 'yes' or 'no'").strip().lower()
    print("\n" * 100)

# Compare bids in dictionary
max_bid = 0
max_bidder_name = ""
for key in bids:
    if bids[key] > max_bid:
        max_bid = bids[key]
        max_bidder_name = key

print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")
