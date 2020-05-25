# Initializing the blockchain list
MINING_REWARD = 10
blockchain = []
genesis_block = {'previous_hash': '',
             'index': 0,
             'transactions': []}
blockchain.append(genesis_block)
continue_displaying_program = True
open_transactions = []
participants = set(['Oslo'])
owner = 'Oslo'


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
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def hash_block(block):
    return '-'.join(str([block[key] for key in block]))


def add_item(recipient, sender=owner, amount=1.0):
    """ Append a new value to the blockchain together with the previous blockchain value.

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default=1.0)
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_new_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {'sender': 'MINING',
                          'recipient': owner,
                          'amount': MINING_REWARD}
    copied_transaction = open_transactions.copy()
    copied_transaction.append(reward_transaction)
    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': copied_transaction}
    blockchain.append(block)
    return True


def get_last_blockchain_item():
    """ Returns the last value of the blockchain """
    if len(blockchain) < 1:
        last_item = None
    else:
        last_item = blockchain[-1]
    return last_item


def get_balance(participant):
    sender = [[transaction['amount'] for transaction in block['transactions'] if transaction['sender'] == participant]
              for block in blockchain]
    open_transactions_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    sender.append(open_transactions_sender)
    amount_sent = 0
    amount_received = 0
    for tx in sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    recipient = [[transaction['amount'] for transaction in block['transactions']
                  if transaction['recipient'] == participant] for block in blockchain]
    for tx in recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent


def display_blockchain_blocks():
    for block in blockchain:
        print(block)


# Output the blockchain list to the console
while continue_displaying_program:
    print("Please choose an option: ")
    print("1: Add a new transaction value")
    print("2: Mine new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("5: Manipulate the chain")
    print("6: Check transaction validity")
    print("7: Quit the program")
    user_input = get_user_option()

    if user_input == 1:
        data = get_user_input()
        recipient, amount = data
        # Add transaction amount to the blockchain
        if add_item(recipient, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_input == 2:
        if mine_new_block():
            open_transactions = []
    elif user_input == 3:
        display_blockchain_blocks()
    elif user_input == 4:
        print(participants)
    elif user_input == 5:
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris',
                                  'recipient': 'Oslo',
                                  'amount': 10}]
            }
    elif user_input == 6:
        if verify_transactions():
            print("All transactions valid")
        else:
            print("There are invalid transactions")

    elif user_input == 7:
        continue_displaying_program = False
    else:
        print("Sorry, you entered an invalid value.")

    if not verify_chain():
        display_blockchain_blocks()
        print("Invalid blockchain")
        break

    print(get_balance(owner))


