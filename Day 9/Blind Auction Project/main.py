# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print("Welcome to the secret auction program!")
auction_name_bid = {}
continue_bidding = True

def find_highest_bidder(auction_name_bid):
    highest_bid = 0
    winner = ""
    for bid in auction_name_bid:
        price = auction_name_bid[bid]
        if price > highest_bid:
            highest_bid = price
            winner = bid

    print(f"The Winner is {winner} with a bid of ${highest_bid}")

while continue_bidding:
    name = input("What is your name?: \n")
    bid_price = int(input("What's your bid?: \n"))
    auction_name_bid[name] = bid_price
    any_other_bidders = input("Are there any other bidders?: Type 'yes' or 'no' \n").lower()
    if any_other_bidders == "no":
        continue_bidding = False
        find_highest_bidder(auction_name_bid)
    elif any_other_bidders == "yes":
        # clear screen
        print("\n" * 10000)

#my code
max_bidder_name = ""
max_bidder_price = 0
max_bid = 0
for bid in auction_name_bid:
    price = auction_name_bid[bid]
    if price > max_bid:
        max_bid = price
        max_bidder_name = bid
        max_bidder_price = price

print(f"The Winner is {max_bidder_name} with a bid of ${max_bidder_price}")


