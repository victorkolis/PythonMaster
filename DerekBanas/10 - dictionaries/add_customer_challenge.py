prompt = ''
customer_list = []
customer = ''
while prompt != 'n':
    prompt = input('Enter Customer(y/n): ').lower()
    if prompt == 'y':
        first_name, last_name = input('Enter Customer: ').title().split()
        customer_list += [{'first_name': first_name, 'last_name': last_name}]

for customer in customer_list:
    print(customer['first_name'], customer['last_name'])
