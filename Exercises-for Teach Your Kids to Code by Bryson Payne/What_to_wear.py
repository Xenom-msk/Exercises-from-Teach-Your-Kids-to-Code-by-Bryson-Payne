# What to wear?
rainy=input("How's the weather? Is it raining? (y/n)").lower()
cold=input("Is it cold today? (y/n)").lower()
if (rainy=='y' and cold=='y'):
    print("You'd better wear a raincoat.")
elif (rainy=='y' and cold!='y'):
    print("Carry an umbrella with you.")
elif (rainy!='y' and cold=='y'):
    print("Put on a jacket, it's cold outside.")
elif (rainy!='y' and cold!='y'):
    print("It's warm outside, put on your favorite fashionable clothes!")
