#define the menu of the restaurant using dictionary
menu={
    'Pizza':180,
    'Burger':60,
    'Pasta':200,
    'Salad':75,
    'Coffee':80,
    'Cold-Drink':45,
    'Lasagne':210,
    'Potato Twister':150
}

#greet and display menu
print("WELCOME TO OUR RESTAURANT!")
print("Pizza: Rs180\nBurger: Rs60\nPasta: Rs150\nSalad: Rs75\nCoffee:80")

#set the default value of order at 0
orderTotal=0

#take input of the item
item1=input("Enter the item you want to order:")

#check if the item is available in the menu
if item1 in menu:
    #if the item is there add item to cart and add in order amount
    orderTotal=+menu[item1]
    print(item1," added to your cart.")

#display a mssg of item unavailable
else:
    print("Ordered item not available.")

#check if the customer wants another item?
#if yes take input for item.
while (1):
    anotherOrder=input("Do you want to add another item? (Yes/No)")
    if anotherOrder=='Yes':
        item2=input("Enter the item you want to order:")
        if item2 in menu:
            orderTotal=+menu[item2]
            print(item2,"added to your order.")
    
    #if no exit the code
    else:
        print("Exiting.")
        break

#print the total order amount
print("Total amount of your order:",orderTotal)