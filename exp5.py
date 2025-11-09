'''Implement a real-time undo/redo system for a text editing application using a Stack data structure. The system should support the following operations:
•	Make a Change: A new change to the document is made.
•	Undo Action: Revert the most recent change and store it for potential redo.
•	Redo Action: Reapply the most recently undone action.
•	Display Document State: Show the current state of the document after undoing or redoing an action
•	Save the document: clear all the undo and redo operations
•	Show undo history: Prints all change in the undo stack.
•	Show redo history : Prints all actions available for redo
•	Revert to Original Document
•	Display all the versions of the document 
'''
def  save():
    version.append(doc)

def make_changes():
    global doc
    undo_stack.append(doc)
    new=input("Enter new doc: ")
    doc=new  
    redo_stack.clear()
    save()
    return doc

def undo():
    global doc
    if not undo_stack:
         print("No more undo possible")
    redo_stack.append(doc)
    doc=undo_stack.pop()
    save()
    print(f"{doc} is new content")

def redo():
    global doc
    if not redo_stack:
        return "No more redo possible"
    undo_stack.append(doc)
    doc=redo_stack.pop()
    save()
    print(f"{doc} is new content")

def display():
    print(doc)

def undo_history():
    for i in undo_stack:
        print(i)

def redo_history():
    for i in undo_stack:
        print(i)

def org_doc():
    print(og_doc)

def versions():
    for i in version:
        print(i)
    return

def revert():
    global doc
    doc=og_doc
    undo_stack.clear()
    redo_stack.clear()
    save()
    print(f"reverted to original -> {doc} with undo stack= {undo_stack} and redo stack={redo_stack}.")

doc=input("Enter your doc: ")
og_doc=doc
undo_stack=[]
redo_stack=[]
version=[doc]
while True:
    print("\n--- Text Editor Menu ---")
    print("1. Make a Change")
    print("2. Undo Action")
    print("3. Redo Action")
    print("4. Display Document State")
    print("5. Display Original doc")
    print("6. Show Undo History")
    print("7. Show Redo History")
    print("8. Revert to Original Document")
    print("9. Display All Saved Versions")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        make_changes()
    elif choice == 2:
        undo()
    elif choice == 3:
        redo()
    elif choice == 4:
        display()
    elif choice == 5:
        org_doc()
    elif choice == 6:
        undo_history()
    elif choice == 7:
        redo_history()
    elif choice == 8:
        revert()
    elif choice == 9:
        versions()
    elif choice == 10:
        print("Exiting editor... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")



