import keyboard

print("")
print("")
print("                     BLOCKMYKEYBOARD")
print("")
print("DON'T CLOSE/MINIMIZED THIS WINDOW DURING THE UTILISATION!")
print("FOR STOP THE BLOCKING, CLOSE THE WINDOW.")
print('Read "About" via BlockMyKeyboard > File > About before use.')

def block_key(event):
    return True
    

keyboard.hook(block_key)

keyboard.wait("") 

