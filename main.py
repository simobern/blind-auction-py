import os
from art import logo
print(logo)

bidding_finished = False
bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ''
  for name in bids:
    bid_amount = bids[name]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = name

  print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))
  bids[name] = bid
  should_continue = input("Are there any other bidder? Type 'yes' or 'no'. ")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == 'yes':
    os.system('clear')