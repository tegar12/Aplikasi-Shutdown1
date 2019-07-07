import os
print("1.Shutdown computer")
print("2.Restart computer")
print("3.Exit")
choice = int(input("Enter your choice : "))

if(choice>=1 and choice<=2):
    if choice == 1:
        os.system("Shutdown /s /t 1")

    elif choice == 2:
        os.system("Shutdown /r /t 1")

    else:
        exit();
