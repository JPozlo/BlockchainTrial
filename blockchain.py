# Initializing the blockchain list
blockchain = []
continue_displaying_program = True

def get_last_blockchain_item():
        """ Returns the last value of the blockchain """
        if len(blockchain) < 1:
            last_item = None
        else:
            last_item = blockchain[-1]
        return last_item


def get_user_input():
    return float(input("Please enter the amount: "))


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


def add_item(previous_transaction):
    """ Append a new value to the blockchain together with the previous blockchain value.

    Argument:
        :previous_transaction: The last blockchain transaction (default [1]).
    """

    if previous_transaction == None:
        previous_transaction = [1]

    blockchain_transaction_amount = get_user_input()
    blockchain.append([previous_transaction, blockchain_transaction_amount])


def display_blockchain_blocks():
    for block in blockchain:
        print(block)


# Output the blockchain list to the console
while continue_displaying_program:
    print("Please choose an option: ")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("3: Manipulate the chain")
    print("4: Quit the program")
    user_input = get_user_option()

    if user_input == 1:
        add_item(get_last_blockchain_item())
    elif user_input == 2:
        display_blockchain_blocks()
    elif user_input == 3:
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_input == 4:
        continue_displaying_program = False
    else:
        print("Sorry, you entered an invalid value.")

    if not verify_chain():
        print("Invalid blockchain")
        break



