sandwiches = ['grilled cheese', 'ruben', 'pb&j', 'philly cheese steak', 'cucumber', 'tuna melt', 'banh mi']

print("These are my sandwiches for sale:")
for sandwich in sandwiches:
    print(f"Delicious sandwich {sandwich}")

for i in range(len(sandwiches)): #1, len(sandwiches) + 1):
    print(f"{i + 1}. {sandwiches[i]}")