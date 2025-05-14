bid_status = True

bids = {}

while bid_status:
    name = input("What is your name?\n")
    bid = int(input("Whai is your Bid amount?\n"))
    
    bids[name] = bid
    
    any_more = input("Are there any more biders. Yes or No?\n").lower()
    
    if any_more == "no":
        bid_status = False
    print("\n"*100)
        
winner =  ""
winning_bid = 0


for bid in bids:
    
    bid_amount = bids[bid]
    if bid_amount > winning_bid:
        winning_bid = bid_amount
        winner = bid 
    
    
print(winner, winning_bid)