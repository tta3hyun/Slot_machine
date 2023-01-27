import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
   
symbol_count = {
    'A': 3,
    'B': 6,
    'C': 9,
    'D': 12,
}

symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
}

def generate_winnings(columns, lines, bet, value):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winnings_lines.append(line + 1)
        
    return winnings, winnings_lines
            
    
def get_slot_spin(rows, cols, symbols):
    symbols_list = []
    for symbol, symbol_count in symbols.items(): 
        for _ in range(symbol_count):
            symbols_list.append(symbol) 
    
    columns = []    
    for _ in range(cols):     
        column = []
        copy_symbols = symbols_list[:] 
        for _ in range(rows):
            value = random.choice(copy_symbols)
            copy_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot(columns):
    print(columns)
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
        
def deposit():
    while True:
        amount = input('What amount of money would you like to deposit?: \n$')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Sorry, your amount must be greater than 0.\n')
        else:
            print('Please enter a number.\n')
    
    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines that you want to bet on (1 - ' + str(MAX_LINES) + '):\n')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Sorry, please enter a valid amount of lines.\n')
        else:
            print('Please enter a number.\n')
    
    return lines    

def get_bet():
    while True:
        amount = input('What amount of money would you like to bet on each line?: \n$')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Sorry, the amount must be between ${MIN_BET}-${MAX_BET}.\n')
        else:
            print('Please enter a number.\n')
    
    return amount
    
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You can not bet more money than you have in your balance.\nYoure current balance is: ${balance} ')
        else:
            break
        
    print(f'You are betting ${bet} on {lines} lines. Your total bet is equal to ${total_bet}.')
    
    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = generate_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines', *winning_lines)

    return winnings - total_bet

def main ():
    balance = deposit()
    while True:
        print(f'Current balance: ${balance}')
        answer = input('Press enter to play (q to quit).')
        if answer == 'q':
            break
        balance += spin(balance)
        
    print(f'You left with ${balance}')

main()
