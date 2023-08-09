import json

def display_menu():
    print(">>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>")
    print("Welcome to Mumbai Munchies Canteen")
    print("1. Add Snack to Inventory")
    print("2. Display the Inventory")
    print("3. Update Snack Quantity")
    print("4. Delete Snack Quantity")
    print("5. Exit")
    print(">>>>>>>>>>>>>>>>>>>>>")
    print(">>>>>>>>>>>>>>>>>>>>>")


option=True


def Load_Inventory():
   try :
       with open("inventory.json","r") as file:
           inventory=json.load(file)
           max_id = max((item["id"] for item in inventory.get("inventory", [])), default=0)
           inventory.setdefault("id", max_id)

   except FileNotFoundError:
       inventory={"id":0}

   return inventory    
   
def Save_Inventory(inventory):
   with open("inventory.json","w") as file:
      json.dump(inventory,file)

def Add_Inventory(inventory):
   inventory["id"] += 1
   snack_name=input("Enter the Snack:")    
   Quantity=input("Enter the Quantity:") 
    
   inventory.setdefault("inventory",[]).append({"id":inventory["id"],"snack":snack_name,"quantity":Quantity})
   print("*************************")
   print("*************************")
   print(f"{Quantity} {snack_name} is added Successfully") 
   print("*************************")
   print("*************************")
   Save_Inventory(inventory)


def update_inventory(inventory):
  new_id=int(input("Enter the id : "))
  
  for item in inventory.get("inventory",[]):
     if(item["id"]==new_id):
        snack=input("Enter the updated snack : ") 
        quantity=input("Enter the updated quantity : ") 
        item["snack"]=snack
        item["quantity"]=quantity
        print(f"{quantity} {snack} is updated successfully")
        Save_Inventory(inventory)
        break

     else: 
        print("Id doesnot match")
        break
            




def main():

   inventory=Load_Inventory()
   while True:
      display_menu()
      choice=input("Enter Your Choice:")
      if(choice=="1"):
         Add_Inventory(inventory)
      elif(choice=="2"):
         print(inventory)    
      elif(choice=="3"):
         update_inventory(inventory)
     
      
      else:
         print("Invalid Choice!!. Please Select the Valid Option")
       

main()

# Add In Inventory


