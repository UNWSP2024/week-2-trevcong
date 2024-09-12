#AUTHOR: Trevor Conger UNWSP
#DATE: 9/8/24
#TITLE: Calculate Total...plus tax

#I dont know if you wanted it this complicated. 


# Functon to calculate the price of 5 items given a selection of 10 items in a store
# After 5 items have been choosen there will be 7% sales tax
def calculate_total_purchase():
                # UNWSP STORE
                # { Item : Price of item }
                # 1: T-shirt , 2: Pull over, 3: Sweatpants, 4: Shorts, 5: Sticker pack
                # 6: Water bottle, 7: Pen pack, 8: Python book, 9: C book, 10: C# book 
    inventoryDict = {1: 25, 2: 35, 3: 45, 4: 25, 5: 10, 6: 15, 7: 5, 8: 105, 9: 150, 10: 125}
    customerOrderFromInvDict = []
    orderValuePreTax = 0
    while(len(customerOrderFromInvDict) < 5):
        try:
            print("Hello! Welcome to the UNWSP clothing store")
            print("Enter a number 1-10")
            print("1: T-shirt, 2: Pull over, 3: Sweatpants, 4: Shorts, 5: Sticker pack")
            print("6: Water bottle, 7: Pen pack, 8: Python book, 9: C book, 10: C# book")
            userSelectionFromDict = int(input("Please enter a number: \n "))
            if (1 <= userSelectionFromDict <= 10):
                customerOrderFromInvDict.append(userSelectionFromDict)
        except ValueError:
            print("This is not a number...")
    for i in range(len(customerOrderFromInvDict)):
        invKeyFromCustomerOrder = customerOrderFromInvDict[i]
        orderValuePreTax += inventoryDict[invKeyFromCustomerOrder]
    finalOrderWithTax = orderValuePreTax * 1.07    
    print(finalOrderWithTax)      


calculate_total_purchase()