class Record:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.next = None

class Student:
    def create_rec(self, head, name, roll, marks):
        if head is not None:
            print("Record already exists! Use insert to add more.")
            return head
        head = Record(name, roll, marks)
        print(f"Record created for {name}.")
        return head
    
    def insert(self, head):
        name = input("Enter name: ")
        roll = int(input("Enter roll no: "))
        marks = float(input("Enter marks: "))
        new_rec = Record(name, roll, marks)

        if head is None:
            head = new_rec
            print(f"Inserted {name} as first record.")
            return head

        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_rec
        print(f"Inserted {name} successfully.")
        return head
    
    def search(self, head, key):
        if head is None:
            print("No records found.")
            return

        temp = head
        found = False
        while temp:
            if temp.name == key or temp.roll == key:
                print(f"Found → Name: {temp.name}, Roll: {temp.roll}, Marks: {temp.marks}")
                found = True
                break
            temp = temp.next
        if not found:
            print("Record not found.")
        return head
    
    def delete(self, head, roll):
        if head is None:
            print("No records found.")
            return head
        
        # if head node itself is to be deleted
        if head.roll == roll:
            print(f"Deleted record of {head.name}.")
            return head.next

        prev = head
        temp = head.next
        while temp:
            if temp.roll == roll:
                print(f"Deleted record of {temp.name}.")
                prev.next = temp.next
                return head
            prev = temp
            temp = temp.next

        print("Record not found.")
        return head
    
    def display(self, head):
        if head is None:
            print("No records to display.")
            return
        temp = head
        print("\n📋 Student Records:")
        while temp:
            print(f"Name: {temp.name}, Roll: {temp.roll}, Marks: {temp.marks}")
            temp = temp.next
        return head

# -------------------------------
# Main program
# -------------------------------
obj = Student()
head = None

while True:
    print("\n1. Create Record\n2. Insert\n3. Search\n4. Delete\n5. Display\n6. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        name = input("Enter name: ")
        roll = int(input("Enter roll no: "))
        marks = float(input("Enter marks: "))
        head = obj.create_rec(head, name, roll, marks)

    elif ch == 2:
        head = obj.insert(head)

    elif ch == 3:
        key = input("Enter name or roll to search: ")
        if key.isdigit():
            key = int(key)
        obj.search(head, key)

    elif ch == 4:
        roll = int(input("Enter roll to delete: "))
        head = obj.delete(head, roll)

    elif ch == 5:
        obj.display(head)

    elif ch == 6:
        print("Exiting...📘")
        break

    else:
        print("Invalid choice!")
