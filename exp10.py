'''
Write a program to represent polynomials using Linked list and perform operations.
Write functions:
a) To input and output polynomials 
b) Evaluates a polynomial at given value of x
c) Add two polynomials
d) Multiplies two polynomials
'''

class Term:
    def __init__(self, coeff, pow):
        self.coeff = coeff
        self.pow = pow
        self.next = None


class Polynomial:

    def create(self, head):
        n = int(input("No of terms in polynomial: "))
        for i in range(n):
            coeff = int(input("Coeff: "))
            pow = int(input("Power: "))
            new = Term(coeff, pow)
            if head is None:
                head = new
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = new
        return head

    def insert(self, head, coeff, pow):
        if head is None:
            self.create(head)
        else:
            temp = head
            while temp.next:
                if temp.pow == pow:
                    temp.coeff += coeff
                temp = temp.next
        return head

    def add(self, poly1, poly2):
        p1 = poly1
        p2 = poly2
        Result = Polynomial()
        while p1 or p2:
            if p2 is None:
                Result.insert(p1.coeff,p1.pow)
                p1=p1.next
            elif p1 is None:
                Result.insert(p2.coeff,p2.pow)
                p2=p2.next
            elif p1.pow>p2.pow:
                Result.insert(p1.coeff,p1.pow)
                p1=p1.next
            elif p1.pow<p2.pow:
                Result.insert(p2.coeff,p2.pow)
                p2=p2.next
            else:
                Result.insert(p1.coeff+p2.coeff,p1.pow)
                p1=p1.next
                p2=p2.next
        return Result

    def multiply(self,poly1,poly2):
        result=Polynomial()
        p1=poly1
        while p1:
            p2=poly2
            while p2:
                coeff=p1.coeff*p2.coeff
                pow=p1.pow+p2.pow
                result.insertNadd(result,coeff,pow)
                p2=p2.next
            p1=p1.next
        return result
    
    def insertNadd(self,result,coeff,pow):
        temp=result
        prev=None
        while temp:
            if temp.pow==pow:
                temp.coeff+=coeff
                return
            prev=temp
            temp=temp.next
        new=Term(coeff,pow)
        if prev is None:
            new.next=result
        else:
            new.next=temp
            prev=new