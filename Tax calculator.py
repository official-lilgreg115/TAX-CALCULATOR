def tax_amount():
    percentage = 5.5/100
    tax=order_amount * percentage
    return tax
def total():
    total_amount = tax_amount() + order_amount
    return total_amount
order_amount = float(input("What is the order amount? "))
state = input('What is the state? ').strip()
if state.lower() == 'wisconsin' or 'wi' :
    tax_amount()
if state.lower() == 'wi':
    print(f'The subtotal is ${order_amount}'
          f'\nThe tax is ${tax_amount()}'
          f'\nThe total is ${total()}')
if state.lower() == 'wisconsin':
     print(f'The subtotal is ${order_amount}'
          f'\nThe tax is ${tax_amount()}'
          f'\n The total is ${total()}')
if state.lower()!= 'wisconsin' or 'wi':
    print(f'The total is ${order_amount}')


