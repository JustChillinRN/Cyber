from stengano import lsb

choice = input("Do you wish to hide or un-hide a hidden message: ")

def decision(decision):
    choice = input("Do you wish to hide or un-hide a hidden message: ")

if choice == "hide":
    image = input("Enter the path to the image: ")
    new_image = input("Enter the name of the final image: ")
    msg = input("Enter your hidden message: ")
    lsb.hide(image, message=msg). save(new_image)
if choice == "un-hide" or choice == "unhide":
    hidden_image = input("Enter the path to the image here: ")
    hmsg = lsb.reveal(hidden_image)
    print(f'Message is {hmsg}')
else:
    print("Try again.")
    decision()

input("Press any key to continue... ")
