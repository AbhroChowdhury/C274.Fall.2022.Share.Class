# Part 2
'''
Taking in an input. Adding words to a list. then looping through the list to see if the word exists
'''
theCount = 0 
word = input("Word: ")
targetWords = ['outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow', 'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots', 'sunny', 'windy', 'coming', 'perfect', 'need', 'sun']
if word in targetWords:
    theCount = theCount + 1
print("Total count %s" % (theCount))
