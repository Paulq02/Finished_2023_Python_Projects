import os
from blind_auction_art import logo
def clear():
    os.system('clear')




bidding_finished=False

bid_log={}

print(logo)

def auction(bidders_name,bid):
    highest_bid=0
    winner=""
    for bidder in bid_log:
        bidders_name=bidder
        bid=bid_log[bidders_name]
        if bid>highest_bid:
            highest_bid=0
            highest_bid=bid
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid} ")


while bidding_finished==False:
    name=input("What is your name?: ")

    bid_amount=int(input("What is your bid?: $"))

    bid_log[name]=bid_amount

    question=input("Are there any other bidders? Type 'yes' or 'no': ")


    if question=="no":
        bidding_finished=True
    else:
        clear()

    
    
auction(bidders_name=name,bid=bid_amount)
    
        

