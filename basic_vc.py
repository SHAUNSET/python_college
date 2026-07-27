def vacuum_simulation():
   
    rooms = {
        "A": True,
        "B": True
    }
    
    print("--- Vacuum Cleaner Simulation ---")
    print(f"Initial State -> Room A: {'Dirty' if rooms['A'] else 'Clean'}, Room B: {'Dirty' if rooms['B'] else 'Clean'}\n")
    

    while rooms["A"] or rooms["B"]:
        print(f"Current Status: Room A is {'Dirty' if rooms['A'] else 'Clean'} | Room B is {'Dirty' if rooms['B'] else 'Clean'}")
        

        choice = input("Which room should be cleaned? (Enter A or B): ").strip().upper()
        
        if choice == "A":
            if rooms["A"]:
                rooms["A"] = False
                print("-> Room A has been cleaned!")
                if rooms["B"]:
                    print("-> Room B is still left dirty.\n")
            else:
                print("-> Room A is already clean!\n")
                
        elif choice == "B":
            if rooms["B"]:
                rooms["B"] = False
                print("-> Room B has been cleaned!")
                if rooms["A"]:
                    print("-> Room A is still left dirty.\n")
            else:
                print("-> Room B is already clean!\n")
        else:
            print("-> Invalid choice. Please enter 'A' or 'B'.\n")
            

    print("--- Target Reached! ---")
    print("Both Room A and Room B are now clean. Vacuum stopping.")


if __name__ == "__main__":
    vacuum_simulation()
