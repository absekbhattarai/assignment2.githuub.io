import msvcrt

print("Welcome to Super Mario!")


print("Press A(to go back) or D(to go front) or W(to jump): ")
print("\n")
print("\t[.][.]")
print("--------------------------")
if msvcrt:
    key = msvcrt.getch().decode("utf-8").lower()
    if key == "w":
        print("\t[.][.]")
        print("\n")
        print("--------------------------")
    elif key == "a":
        print("\n")
        print("[.][.]")
        print("--------------------------")
    elif key == "d":
        print("\n")
        print("\t\t[.][.]")
        print("--------------------------")

