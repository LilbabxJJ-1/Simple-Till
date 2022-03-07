#Items bought
items = {4062: "Cucumber", 4087: "Roma Tomato", 3082: "Broccoli", 4681: "Green Bell Peppers", 5101: "Bollio", 4889: "Cilantro"}
#Prices (Made up)
prices = {"Cucumber": .33, "Roma Tomato": .99, "Broccoli":.50} #etc..
#Category of the Item
item_cate = {"Cucumber": "quantity", "Roma Tomato": "weight", "Broccoli":"weight"} #etc..

#User Input
script = True
while script:
     #Asking for the PLU code until it finds one within the "items" dictionary
     usript = int(input("PLU code..? "))
     if usript in items:
       fruit = items.get(usript)
       break
     else:
       print("Item not found") #If not in the dictionary

#Gets price the user will recieve based qauntity or weight
quantity = "N/A"
weight = "N/A"
if item_cate.get(fruit) == "quantity":
 while True:
  try:
    quantity = int(input("How many do you have? "))
    break
  except ValueError:
      print("You can only use whole numbers!")
else:
   weight = float(input("How many pounds? "))

#Calculate the price based on item, cost, and amount
def price(usript, quantity, weight):
   prc = prices.get(fruit)
   if item_cate.get(fruit) == "quantity":
     total = prc * quantity
   else:
      total = prc * weight
   return total
ppc = price(usript, quantity, weight)

#Prints the item and the final price 
def reciept(item, price):
  if item_cate.get(fruit) == "quantity": 
    print(f"{quantity} {fruit}s - ${round(ppc, 2)}")
  else:
    print(f"{weight} pounds | {fruit} - ${round(ppc, 2)}")
reciept(items.get(usript), price(usript, quantity, weight))