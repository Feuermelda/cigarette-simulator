
cig_filter = 15  # filter of cigarette
total_ash = 0


def smoke_flick(choice, left, cig_ash, total_cig):

    if choice == 1:

        cig_ash = cig_ash + 5
        left = total_cig - cig_ash

        if cig_ash >= 20:

            total_cig = left
            cig_ash = 0

    elif choice == 2:

        total_cig = left
        cig_ash = 0

    return f"\033[33m{'█'*cig_filter}\033[0m{'█'*left}\033[91m{'█'}\033[0m{'░'*cig_ash}", left, cig_ash, total_cig


smoking = True
rest = 45
new_total = 45
ash = 0

print("\n\n--- Welcome to the cigarette simulator ---\n\n")
print(f"\033[33m{'█'*cig_filter}\033[0m{'█'*new_total}")

input("\nPress any key to ignite the cigarette...")
print(f"\033[33m{'█'*cig_filter}\033[0m{'█'*(new_total-1)}\033[91m{'█'}\033[0m")

while smoking:
    user = input("\nPress D for Drag, F for Flicking Ash:\n").strip().lower()
    if user == "d":
        userchoice = 1

    elif user == "f":
        userchoice = 2

    else:
        print("Unknown command.")
        continue
    cigarette, rest, ash, new_total = smoke_flick(
        userchoice, rest, ash, new_total)

    print(cigarette)
    if rest == 0:

        print("\nYou done smoking!\n")
        print(f"\033[33m{'█'*cig_filter}\033[0m")
        smoking = False
