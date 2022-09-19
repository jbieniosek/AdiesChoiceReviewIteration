import random

sandwiches = ['grilled cheese', 'ruben', 'pb&j', 'philly cheese steak', 'cucumber', 'tuna melt', 'banh mi']

print("These are my sandwiches for sale:")
for sandwich in sandwiches:
    print(f"Delicious sandwich {sandwich}")

for i in range(len(sandwiches)): #1, len(sandwiches) + 1):
    print(f"{i + 1}. {sandwiches[i]}")

sandwich_prices = {}
price_range = (1, 10)
for sandwich in sandwiches:
    sandwich_prices[sandwich] = random.randint(price_range[0], price_range[1])

print(sandwich_prices)

for sandwich,price in sandwich_prices.items():
    print(f"{sandwich} ${price}")

display_list = []
for target_price in range(price_range[0], price_range[1] + 1):
    for sandwich,price in sandwich_prices.items():
        if price == target_price:
            display_list.append(sandwich)

print(display_list)
display_num = 1
for sandwich in display_list:
    price = sandwich_prices[sandwich]
    print(f"{display_num}. {sandwich} ${price}")
    display_num += 1

    
