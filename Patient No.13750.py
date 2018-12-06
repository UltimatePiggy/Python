day=1
cure=0
invention="no"
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
print("Welcome doctor!")
print("You are in control of Patient No.13750!")
print("He has a disease without a cure!")
print("You cannot cure the disease, you will have to wait a certain amount of days for a cure!")
print("The amount of days depends on your difficulty.")
print("KEEP HIM ALIVE!")
print("FOR YOUR OWN SANITY, I NEED TO MENTION THAT ALL CHOICES ARE LUCK BASED!")
print("PLEASE DOUBLE CHECK ANSWERS, AS AN INVALID ANSWER WILL CLOSE THE APPLLICATION")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Please choose the game difficulty!")
print("Choice 1: Easy")
print("Choice 2: Medium")
print("Choice 3: Hard")
difficulty=input("Please enter your choice number: ")
if difficulty=="1":
    stability=200
    happiness=200
    budget=200
    health=200
    print("Easy Selected!")
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")
elif difficulty=="2":
    stability=100
    happiness=100
    budget=100
    health=100
    print("Medium Selected!")
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")
elif difficulty=="3":
    stability=75
    happiness=75
    budget=75
    health=75
    print("Hard Selected!")
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")
else:
    print("Invalid Answer!")
    stability=75
    happiness=75
    budget=75
    health=75
    difficulty=3
    print("Hard Selected!")
    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")
print("\n")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invented:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 1
print("Day 1:Patient No.13750 has developed a cough, we should give him medication!")
print("Should we give him medication 4528 or medication 8245?")
medication=input("4528 or 8245?")
if medication=="4528":
    print("Great Choice!")
    print("Your Budget -3")
    print("That fills the patient with hope!")
    budget=budget-3
    happiness=happiness+7
elif medication=="8245":
    print("That is the swelling medication!")
    print("Patient Stability-15")
    stability=stability-15
    print("Your Budget-5")
    budget=budget-5
    print("Patient Happiness-5")
    happiness=happiness-5
else:
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 2
print("The patient has asked for some food!")
print("Choice 1:A Milk Chocolate Cake!")
print("Choice 2:A Salad!")
print("Choice 3:A Triple Milk Chocolate Fudge Brownie with a cherry on top!")
print("Please type the choice number!")
food=input("1,2 or 3?")
if food=="1":
    print("He is lactose intolerant!")
    print("Terrible Choice!")
    stability=stability-15
    health=health-10
    happiness=happiness-10
    print("You are lucky he didn't die!")
    print("Patient Stability-15")
    print("Patient Health-10")
    print("Patient Happiness-10")
elif food=="2":
    print("He is lactose intolerant!")
    print("Great Choice!")
    print("That really brightens the mood!")
    stability=stability+5
    print("Stability+5")
    happiness=happiness+10
    print("Happiness+10")
elif food=="3":
    print("He is lactose intolerant!")
    print("Terrible Choice!")
    stability=stability-15
    health=health-10
    happiness=happiness-10
    print("You are lucky he didn't die!")
    print("Patient Stability-15")
    print("Patient Health-10")
    print("Patient Happiness-10")
else:
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 3
print("An infection has grown in the patient's Lower Leg!")
print("It needs desperate medical attention!")
print("Choice 1: Amputate the infected leg!")
print("Choice 2: Give the patient some antibiotics!")
infection=input("Choice 1 or Choice 2?")
if infection=="1":
    print("That was very unnecessary, at least the infection is gone!")
    print("The Patient is very upset about the lost leg!")
    print("Patient Happiness-15")
    happiness=happiness-15
    print("Your Budget-5")
    budget=budget-5
    print("Patient Stability+10")
    stability=stability+10
elif infection=="2":
    print("Great Choice!")
    print("The infection is clearing.")
    print("Patient Happiness+10")
    happiness=happiness+10
    print("Patient Stability+5")
    stability=stability+5
    print("Your Budget-2")
    budget=budget-2
else:
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 4
print("The patient requests a family visit!")
print("Choice 1:Allow the visit.")
print("Choice 2:Decline the visit.")
print("Choice 3:Ignore the patient completely.")
fv=input("Choice 1, Choice 2 or Choice 3?")
if fv=="1":
    print("The patient is happy!")
    print("His family is now infected with the virus,")
    print("You hire a doctor to care for the family!")
    print("Patient Happiness+5")
    happiness=happiness+5
    print("Your Budget-20")
    budget=budget-20
elif fv=="2":
    print("The patient is dissapointed but you explain why you declined,")
    print("He understands your choice!")
    print("Patient Happiness-2")
    happiness=happiness-2
elif fv=="3":
    print("The patient knows you heard him,")
    print("he is filled with stress and rage!")
    print("Patient Happiness-10")
    happiness=happiness-10
    print("Patient Stability-10")
    stability=stability-10
else:
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 5
print("The Patient requests a different drink than water!")
print("Choice 1: Decline the request but explain why.")
print("Choice 2: Milk.")
print("Choice 3: Decline the request.")
print("Choice 4: Coca-Cola.")
drink=input("Please enter the choice number: ")
if drink=="1":
    print("Correct Answer!")
    print("The patient is unhappy but, he understands.")
    print("Patient Happiness-5")
    happiness=happiness-5
elif drink=="2":
    print("That was a catastrophic desicion!")
    print("The patient is lactose intolerant.")
    print("Patient Health-10")
    health-=10
elif drink=="3":
    print("The patient is dissapointed as you didn't give a reason!")
    print("You did the right thing but, maybe think about the patient's happiness next time!")
    print("Patient Happiness-15")
    happiness-=15
elif drink=="4":
    print("That is very unhealthy, at least you didn't choose milk!")
    print("He is lactose intolerant.")
    print("Patient Happiness+5")
    happiness+=5
    print("Patient Stability-7")
    stability-=7
    print("A Coca-Cola advertiser was strolling through the hospital until he saw the patient")
    print("He asks if he can film this for an advert, do you agree?")
    print("Choice 1:Yes")
    print("Choice 2:No")
    advert=input("Please enter the choice number: ")
    if advert=="1":
        print("You have been generously paid!")
        print("Your Budget+20")
        budget+=20
    elif advert=="2":
        print("You was going to be generously paid!")
        print("The patient always wanted to be on TV.")
        print("Patient Happiness-5")
        happiness-=5
    else:
        print("Invalid Answer!")
        exit()
else:
    print("Invalid Answer!")
    exit()
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 6
print("The patient is in a lot of pain!")
print("He wants you to pull the plug.")
print("Choice 1: Pull the plug and watch him die!")
print("Choice 2: Don't pull it!")
print("Choice 3: Tell him to wait 24 days.")
suicide=input("Please enter your choice number!")
if suicide=="1":
    print("It was the right thing to do.")
    print("But pulling the plug only turns the machines off!!")
    print("Patient Stability=0")
    stability=0
    print("Patient Happiness+10")
    happiness+=10
elif suicide=="2":
    print("He tries to pull it himself but falls while leaning over the machine!")
    print("Patient Health-10")
    health-=10
    print("Patient Happiness-10")
    happiness-=10
elif suicide=="3":
    print("He tries to pull it himself but falls while leaning over the machine!")
    print("Patient Health-10")
    health-=10
    print("Patient Happiness-10")
    happiness-=10
else:
    print("Invalid Answer!")
    exit()
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 7
print("You catch the patient drinking alcohol!")
print("Choice 1:Let Him Off.")
print("Choice 2:Take it all immediately.")
alco=input("Please type your choice number.")
if alco=="1":
    print("He appreciates your co-operation!")
    print("Patient Happiness+10")
    print("Patient Stability-10")
    happiness=happiness+10
    stability=stability-10
elif alco=="2":
    print("He tries to attack you!")
    print("You fail to take the alcohol away.")
    print("Patient Happiness-5")
    print("Patient Stability-15")
    stability=stability-15
    happiness=happiness-5
else:
    print("Invalid Answer!")
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 8
print("An expensive surgery is needed.")
print("Without the surgery the patient's stability will massively drop!")
print("Choice 1: Expensive Surgery.")
print("Choice 2: No Surgery.")
surgery=input("Please enter your choice number: ")
if surgery=="1":
    print("The patient's stability is rising!")
    print("Your Budget-20")
    print("Patient Stability+15")
    budget-=20
    stability+=15
elif surgery=="2":
    print("The Patient's Stability is dropping!")
    print("Your Budget+15")
    print("Patient Stability-20")
    budget+=15
    stability-=20
else:
    print("Invalid Answer")
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 9
print("The patient asks for a bit of privacy!")
print("Choice 1: Let him do whatever he wants.")
print("Choice 2: Explain that you need to be by his side at all times.")
privacy=input("Please enter your choice number.")
if privacy=="1":
    print("You hear a gunshot...")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("You open the curtain...")
    print("\n")
    print("\n")
    print("He's dead!")
    print("Patient stability=0")
    print("Patient Happiness=0")
    print("Patient Health=0")
    stability=0
    happiness=0
    health=0
elif privacy=="2":
    print("You tell him the hospital policy!")
    print("You call security to search the patient...")
    print("\n")
    print("He has a gun.")
    print("You ask why.")
    print("He says he was going to shoot himself.")
    print("He is now put on high security.")
    print("Patient Happiness-15")
    print("Your Budget-5")
    happiness-=15
    budget-=5
else:
    print("Invalid Answer")
    exit(0)
if stability<1:
    print("The patient is dying!")
    health=health-25
elif stability>0:
    print("\n")
else:
    print("\n")
if happiness<1:
    print("The patient is depressed!")
elif happiness>99:
    print("Hope is in the air!")
    print("\n")
else:
    print("\n")
if budget<1:
    print("You have no money!")
    print("The life support machines are shutting down!")
    stability=stability-10
elif budget>99:
    print("\n")
    budget=budget-5
else:
    print("\n")
if health<1:
    print("Game Over! Patient No.13750 is dead!")
    exit(0)
elif health>99:
    print("\n")
else:
    print("\n")
if difficulty=="1":
    if invention=="yes":
        print(" ")
    elif invention=="no":
        if difficulty=="1":
            if day>29:
                cure=6
                invention=yes
            else:
                print(" ")
        elif difficulty=="2":
            if day>34:
                cure=7
                invention=yes
            else:
                print(" ")
        elif difficulty=="3":
            if day>39:
                cure=8
                invention=yes
            else:
                print(" ")
        else:
            print("It Appears the game has crashed!")
            print("How Embarassing!")
    else:
        print("It Appears the game has crashed!")
            print("How Embarassing!")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    cure=cure-1
elif invention=="no":
    print(" ")
else:
    print("It appears the game has crashed!")
    print("How Embarassing!")
    exit(0)
if invention=="yes":
    if cure<1:
        print("You Win!")
    else:
        print(" ")
elif invention=="no":
    if cure<1:
        cure="unavailable"
    else:
        print(" ")
else:
    print("It appears the game has crashed!")
    print("How embarassing!")
day=day+1
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("Patient Stability:",stability)
print("Patient Happiness:",happiness)
print("Patient Health:",health)
print("Your Budget:",budget)
print("Day:",day)
print("Cure Invention:",invention)
print("Days Until Win:",cure)
print("\n")
print("Keep the stability high because if it reaches 0, the patient will start to die!")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
#Day 10
print("The patient has developed a small swelling in his neck.")
print("Should we give him medication 4528 or medication 8245?")
necswel=input("4528 or 8245: ")
if necswel=="4528":
    print("That is the cough medication.")
    print("Wrong choice!")
    print("Patient Stability-7")
    stability-=7
elif necswel=="8245":
    print("Correct, this is the swelling medication.")
    









