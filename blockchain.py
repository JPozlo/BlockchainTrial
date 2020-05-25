# Initializing the blockchain list
blockchain = []
genesis_block = {'previous_hash': '',
             'index': 0,
             'transactions': []}
blockchain.append(genesis_block)
continue_displaying_program = True
open_transactions = []
owner = 'Oslo'


def get_last_blockchain_item():
        """ Returns the last value of the blockchain """
        if len(blockchain) < 1:
            last_item = None
        else:
            last_item = blockchain[-1]
        return last_item


def get_user_input():
    """ Returns a tuple containing amount and recipient of a transactions: (recipient, amount) """
    recipient_input = input("Enter the recipient of the transaction: ")
    amount_input = float(input("Please enter the transaction amount: "))
    return recipient_input, amount_input


def get_user_option():
    user_choice = input("Choose your option: ")
    return int(user_choice)


def verify_chain():
    """ Returns True or False depending on verifiability of the blockchain """
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
                continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


def add_item(recipient, sender=owner, amount=1.0):
    """ Append a new value to the blockchain together with the previous blockchain value.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default=1.0)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_new_block():
    last_block = blockchain[-1]
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block += str(value)
    block = {'previous_hash': 'XYZ',
             'index': len(blockchain),
             'transactions': open_transactions}
    blockchain.append(block)
    print(hashed_block)


def display_blockchain_blocks():
    for block in blockchain:
        print(block)


# Output the blockchain list to the console
while continue_displaying_program:
    print("Please choose an option: ")
    print("1: Add a new transaction value")
    print("2: Mine new block")
    print("3: Output the blockchain blocks")
    print("4: Manipulate the chain")
    print("5: Quit the program")
    user_input = get_user_option()

    if user_input == 1:
        data = get_user_input()
        recipient, amount = data
        # Add transaction amount to the blockchain
        add_item(recipient, amount=amount)
        print(open_transactions)
    elif user_input == 2:
        mine_new_block()
    elif user_input == 3:
        display_blockchain_blocks()
    elif user_input == 4:
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_input == 5:
        continue_displaying_program = False
    else:
        print("Sorry, you entered an invalid value.")

    # if not verify_chain():
    #     print("Invalid blockchain")
    #     break



