food = {}  # creating food called dictionary
food["Toad in a Hole"] = "England"
food["Pizza"] = "Italy"
food["Xiao Long Bao"] = "China"
food["Poutine"] = "Canada"
food["Haggis"] = "Scotland"
print("food:  ", food)  
print()

food2 = { "Xiao Long Bao":"China", "Pizza":"Italy", "Poutine":"Canada", "Toad in a Hole":"England", "Haggis":"Scotland" }  # another way of setting key value pairs in a dictionary
print("food2: ", food2)
for i in food2.keys():  # loop through all the keys and print them 
    print(i)
print()
for i in food2.values():  # returns the values of the keys
    print(i)
