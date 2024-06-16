# Importing necessary modules
# MOHAMED NASRAOUI
from datetime import datetime
from interpreter import Interpreter
import readline

# Initializing variables
running = True
verbose = False
current_time = datetime.now().strftime("%b %-d %Y, %H:%M:%S:%f")
print("NAS processor emulator 1.0 ({})\nType 'help' for more information.".format(current_time))

# Main loop for user interaction
while running == True:
    cmd = input("NAS::").lower()
    
    # Exiting the emulator
    if cmd=="exit" :
        print("Exiting...")
        running = False

    # Displaying help information
    elif cmd=="help":
        print("NAS Processor Emulator Help:")
        print("--------------------------------------------------")
        print("Commands available:")
        print("  HELP\t\tDisplay this help message.")
        print("  EXIT\t\tExit the emulator.")
        print("  CONFIG\tChange current configuration.")
        print("  RUN\t\tLoad and execute instructions from a source file.")
        print()
        print("Instructions in source file:")
        print("  Each line of the source file should contain an instruction to be executed.")
        print("  Instructions must be compatible with the NAS processor's instruction set.")
        print("  Follow the syntax given in the file help.nas.")

    # Configuring emulator settings
    elif cmd=="config":
        ans = input("Enable verbose ?(Y\\n)").lower()
        if ans=="y":
            verbose = True
            print("Verbose mode enabled !")
        else :
            verbose = False
            print("Verbose mode disabled !")

    # Running instructions from a source file
    elif cmd=="run" :
        code = input("\tSource file to emulate : ")
        try:
            with open(code, 'r') as file:
                pass
        except Exception:
            print(">>>EmulatorError: File Not Found")
        else:
            interpreter = Interpreter(code, verbose)
            interpreter.run()
