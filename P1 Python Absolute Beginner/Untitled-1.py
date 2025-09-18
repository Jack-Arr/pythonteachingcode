# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return f"{fish} costs {price}" 
# gathering input
fish_entry = input("Enter fish type ")
price_entry = input("Enter the price ")


# full name
name = "Jack Arrington"
# final print with full name and fishstore results
print("Report for", name + ".", "Fish Type:", fishstore(fish_entry, price_entry))