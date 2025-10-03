"# Zakaria Ahmed"

admins = ['Ahmed', 'Zakaria', 'Mohamed', 'Nader', 'Mahmoud', 'Mohanad']
name = input("enter your name: ".title()).strip().capitalize()
if name in admins:
    print(f"Hello {name}, welcome back".capitalize())
    option = input(
        "enter your option are you want to update or delete your name or nothing: ").lower().strip()
    if option == 'nothing':
        exit(0)
    elif option == 'delete':
        admins.remove(name)
    elif option == 'update':
        newName = input("Enter your new name plz: ").strip()
        index = admins.index(name)
        admins[index] = newName
        print("your name is updated successfully.".capitalize())
    else:
        print("invalid input!!!".title())
else:
    print("You don't an admin")
    choice = input("Do you want to become admin in group(Yes (Y) or No (N))?".title(
    )).capitalize().strip()
    if choice == 'Y' or choice == 'Yes':
        print("You become now an admine")
        admins.append(name)
    else:
        print("You are not added.".capitalize())
print(admins)
