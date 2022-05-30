'''
처음 표의 행 개수를 나타내는 정수 n, 처음에 선택된 행의 위치를 나타내는 정수 k, 수행한 명령어들이 담긴 문자열 배열 cmd가 
매개변수로 주어질 때, 모든 명령어를 수행한 후 표의 상태와 처음 주어진 표의 상태를 비교하여 삭제되지 않은 행은 O, 
삭제된 행은 X로 표시하여 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
'''

class Node:
    def __init__(self, value, prev):
        self.data = value
        self.prevNode = prev
        self.nextNode = None

delStack = []
head = None
select = None

def processOrder(order, answer):
    global head, select

    char = order[0]
    if len(order) > 1:
        val = int(order[2:])

    if char == 'U':
        for i in range(val):
            select = select.prevNode
    elif char == 'D':
        for i in range(val):
            select = select.nextNode
    elif char == 'C':
        delStack.append(select)
        answer[select.data] = 'X'
        #if select is head
        if select.prevNode == None:
            head = select.nextNode
            head.prevNode = None
            select = head
        
        #if select is tail
        elif select.nextNode == None:
            select.prevNode.nextNode = None
            select = select.prevNode

        else:
            select.prevNode.nextNode = select.nextNode
            select.nextNode.prevNode = select.prevNode
            select = select.nextNode

    else:
        popped = delStack.pop()
        #if popped node is head
        if popped.prevNode == None:
            popped.nextNode.prevNode = popped
        elif popped.nextNode == None:
            popped.prevNode.nextNode = popped
        else:
            popped.prevNode.nextNode = popped
            popped.nextNode.prevNode = popped
        answer[popped.data] = 'O'
            

def solution(n, k, cmd):
    global head, select
    answer = ['O'] * n
    head = Node(0,None)
    select = head
    for i in range(1,n):
        select.nextNode = Node(i, select)
        select = select.nextNode
    
    select = head
    for i in range(k):
        select = select.nextNode

    for order in cmd:
        processOrder(order, answer)


    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))