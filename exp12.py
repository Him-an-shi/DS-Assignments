'''
12	A university library wants to maintain a catalog of up to 100 different reference books using their accession numbers (unique keys for each book). The library system must handle rapid addition, lookup, and removal of books as books are acquired or removed over time. Design and implement a hash table of fixed size to manage the library's reference book catalog using accession numbers as unique keys. The hash table should:
•	Allow the library staff to insert a new accession number when a book is added.
•	Search for a book using its accession number and report its status (found/absent).
•	Delete a book’s record using its accession number when the book is removed or lost.
•	Display the complete state of the hash table with all stored accession numbers.
Your hash table should use the division method for hashing and linear probing(without replacement and with replacement) for handling collisions.  
'''
def without_rep(table,accNo):
    for i in range(len(table)):
        idx=(i+accNo)%len(table)
        while table[idx]==-1 or table[idx]==-2:
            table[idx]=accNo
            print(f"inserted {accNo} at {idx}")
            return table
    print("Hash Table is full")
    return table

def with_rep(table,accNo):
    for i in range(len(table)):
        idx=(i+accNo)%len(table)
        if table[idx]==-1 or table[idx]==-2:
            table[idx]=accNo
            print(f"inserted {accNo} at {idx}")
            return table
        exist=table[idx]
        exist_idx=exist%len(table)
        if exist_idx!=idx:
            table[idx] = accNo
            return with_rep(table, exist)
    return table

def search(table,accNo):
    for i in range(len(table)):
        idx=(i+accNo)%len(table)
        if table[idx]==accNo:
            print(f"{accNo} found at index {idx}")
    return table

def delete(table,accNo):
    for i in range(len(table)):
        idx=(i+accNo)%len(table)
        if table[idx]==accNo:
            table[idx]=-2
            print(f"{accNo} deleted from index {idx}")
    return table

table=[-1]*10
while True:
    accNo=int(input())
    print(without_rep(table,accNo))
    print(with_rep(table,accNo))
    print(search(table,accNo))
    print(delete(table,accNo))