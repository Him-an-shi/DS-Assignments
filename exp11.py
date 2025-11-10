'''
11	A university library wants to maintain a catalog of up to 100 different reference books, identified by unique accession numbers.
 The system must support rapid addition, lookup, and removal of books as they are acquired or removed.
   Design and implement a hash table with separate chaining to manage the library’s reference book catalog, using accession numbers as unique keys. 
   Requirements: The hash table should have a fixed number of 10 rows (buckets), each represented as a dynamic list (or a linked list). 
   Each row (bucket) stores all books whose accession numbers hash to that bucket, allowing efficient handling of collisions.
New books can be inserted, searched, or deleted in the catalog based on accession number.
The staff should be able to:
Insert a new accession number for each new book.
Search for a book by accession number and report its status.
Delete a book’s record when withdrawn/lost.
Display the entire hash table with all stored accession numbers in each bucket.
The hash function should use the division method:
bucket_index = accession_number %10 
'''
table=[[] for i in range(10)]
accNo=int(input())
def insert(table,accNo):
    idx=accNo%10
    table[idx].append(accNo)
    return table
def delete(table,accNo):
    idx=accNo%10
    for i in range(len(table[idx])):
        if table[idx][i]==accNo:
            table[idx].pop(i)
            return "Done"
    return "Nope"


    
print(insert(table,accNo))
print(delete(table,accNo))
