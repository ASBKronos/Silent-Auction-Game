import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def find_highest_bid(bid_records):
    max = 0
    winner = ''
    for i in bid_records:
        bid_amount = bid_records[i]
        if bid_amount > max:
            max = bid_amount
            winner = i
    print(f'The winner is {winner} with a bid of ${max}')


print(logo)
bidder = {}

end_of_bid = False

while not end_of_bid:

    name = input("Enter the bidder name: ")
    price = int(input("Enter the bid amount: $"))
    bidder[name] = price

    choice = input("Do you want to enter another bidder? Enter either 'y' or 'n': ").lower()
    if choice == 'n':
        end_of_bid = True
        find_highest_bid(bidder)
    elif choice == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')

