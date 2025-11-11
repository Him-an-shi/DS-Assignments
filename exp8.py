'''A call center receives incoming calls, and each call is assigned a unique customer ID. 
The calls are answered in the order they are received. Consider multiple operators are available to answer the calls. 
.Each operator has their own call queue.A new call is assigned to the operator whose total queued call time is lowest.
 Your task is to simulate the load -balanced call queue of a call center using a queue data structure.
• addCall(customerID, callTime): Add a call to the queue with the customer ID and the
call time (in minutes).
• answerCall(): Answer and remove the first call from the queue.
• viewQueue(): View all calls currently in the queue without removing them.
• isQueueEmpty(): Check if the queue is empty.
Call Logs: Store and print call history per operator.
Average Waiting Time per Operator (Based on queued calls).
Next Available Operator Time: Predict when an operator becomes free.
viewLongestWaitingCallPerOperator: Determine the call that has been waiting the longest. Display the customer ID, call time, and how long the call has been waiting.
'''
n=int(input("Enter number of Operators: "))
operators=[[] for _ in range(n)]
call_log=[[] for _ in range(n)]

def total_time(queue):
    total=0
    for call in queue:
        total+=call[1]
    return total

def least_busy():
    total_time_list=[]
    for queue in operators:
        total_time_list.append(total_time(queue))
    min_time=min(total_time_list)
    idx=total_time_list.index(min_time)

def addCall(customerID, callTime):
    op_idx=least_busy()
    operators[op_idx].append(customerID, callTime)
    return operators[op_idx]

def answerCall(opID):
    call=operators[opID].pop(0)
    call_log.append(call)
    return call_log

def viewQueues():
    for  queue in operators:
        print(queue)

def  emptyQueue():
    for queue in operators:
        if not queue:
            print(f"operator {operators.index(queue)} is empty")

def callLogs():
    for call in call_log:
        print(call)

def avgWatingTime():
    waitingTime=[]
    for queue in operators:
        waitingTime.append(total_time(queue)/len(queue))
    print(waitingTime)

def nextAvailable():
    for queue in operators:
        print(total_time(queue))

def longestWatingTime():
    for call in call_log:
        print(call[1])

customerID=input()
callTime=int(input())
opID=int(input())
print(addCall(customerID,callTime))
print(answerCall(opID))