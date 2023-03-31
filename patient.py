


def calculate_bill(name, cleaning, cavity_filling, Xray):
    Total=0
    Tax=0
    Cleaning_rate = 60
    cavity_filling_rate = 200
    Xray_rate = 100
    tax_rate = (15/100)
    Subtotal = 0
    if cleaning == "y":
        Subtotal = Subtotal+Cleaning_rate
    elif cleaning =="n":
        Subtotal = Subtotal

    if cavity_filling == "y":
        Subtotal = Subtotal+cavity_filling_rate
    elif cavity_filling == "n":
        Subtotal = Subtotal

    if Xray == "y":
        Subtotal = Subtotal+Xray_rate
    elif Xray =="n":
        Subtotal = Subtotal

    
    Tax = Subtotal * tax_rate
    Total = Subtotal + Tax
        
    if Total > 300:
        Total *= 0.9
    elif Total > 200:
        Total *= 0.95
    
#receipt print

    print("Melanie Dental Clinic")
    print("* ----------------------------*")
    print("Receipt for patient name:" ,name)
    print("----------------------------------------------")
    print("Subtotal" ,Subtotal)
    print("Tax" ,Tax)
    print("------------------------------------------------")
    print("Total" ,Total)

#get from user
name = input("Enter patient's name:")
cleaning = input("Was cleaning performed? (y/n):")
cavity_filling = input("Was cavity-filling performed? (y/n):")
Xray = input("Was X-Ray performed? (y/n):")

calculate_bill(name, cleaning, cavity_filling, Xray)

    

   