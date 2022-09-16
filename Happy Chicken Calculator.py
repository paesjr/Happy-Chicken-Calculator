Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Software title 
print("");
print("廾闩尸尸丫 ⼕卄讠⼕长🝗𝓝  ⼕闩㇄⼕ㄩ㇄闩〸ㄖ尺");
print(""); 

number_chicken = float(input('\tHow many chickens do you have? '))
print("")

total_feed = 120 * int(number_chicken)

print(f'You need to feed {total_feed} grams of pellets to your chickens per day.')

print("");
print("\tWhat size is your bag of chicken pellets?");
print("");
kilograms = float(input("Enter Kilogram Value: ")) 

grams = float(kilograms * 1000)
serving = float(grams / 120)

print("");
print("\tHow much are you paying for your bag of chicken pellets?");
print("");
price = float(input("Enter Price Value: $"))

serving_cost = float(price / serving)

print("");3
print("\tHow many eggs are you collecting per day?");
print("");
egg_number = float(input("Enter the number of eggs: "))

egg_cost = float((serving_cost * number_chicken) / egg_number)
print("")
print(f"\tYou are spending approximately ${(format(egg_cost,'.2f'))} worth of feed per egg.")
print("")

reminder = print("Would you like us to send you a reminder a week before you run out of pellets through text message?")
print("")

while True:
    value = input("yes or no:").lower()
    if value == "yes":
      phone_number = input('Please enter a phone number in the format XXX-XXXX-XXXX: ')
      break
    if value == "no": 
      break
       
       
print("")
print("")
print("\tThanks for using the Happy Chickens Calculator! :)")
