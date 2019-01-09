class LinkedList:
    def __init__(s):
        s.head=ListNode()

    def __str__(self):
        a=""
        curr=self.head.next
        while(curr!=None):
            a=a+str(curr.value)+" "
            curr=curr.next
        return a


    def insert(s,x,pos):
        if(pos==s.head):
            temp=ListNode()
            temp.next=pos.next
            temp.value=x
            pos.next=temp
            #s.PrintList()

        elif(pos.next==None and pos.value!=None):
            pos.next=ListNode()
            pos.next.value=x
            pos=pos.next

        else:
            t=ListNode()
            t.next=pos.next
            pos.next=t
            t.value=x
    def delete(s,pos):
        if(pos==s.head):
            s.head.next=s.head.next.next
        else:
            pos.next=pos.next.next
    def PrintList(s):
        i=1
        pos=s.head.next
        while(1):
            print("value at ",i," is:",pos.value)
            i=i+1       
            pos=pos.next
            if(pos==None):
                break;
    def search(s,x):
        i=1
        flag=0
        pos=s.head.next
        while(1):
            if(pos.value==x):
                print('value ',x,' found at ',i)
                flag=1
                break;
            i=i+1       
            pos=pos.next
            if(pos==None):
                break;
        if(flag==0):
            print("Element ",x," not found")
    def isEmpty(s):
        if(s.head.next==None):
            return True
        else:
            return False
    def len(s):
        i=0
        pos=s.head.next
        if(s.head.next!=None):
            while(1):
                i=i+1       
                pos=pos.next
                if(pos==None):
                    break;
        return i
    def insertAtindex(s,x,i):
        j=1
        flag=0
        pos=s.head.next
        while(j<i and i!=0):
            pos=pos.next
            j=j+1
            if(pos==None):
                flag=1
                break;            
        if(flag==0):
            if(i==0):
                pos=s.head
            s.insert(x,pos)     
        if(flag==1):
            print('List indexing out of bounds')


class ListNode:
    def __init__(s):
        s.value=None
        s.next=None
        s.key=None
        

# n1=LinkedList()
# # n1.insert(0,n1.head)
# # n1.insert(6,n1.head)
# # n1.insert(123,n1.head)
# # n1.insert(999,n1.head.next)
# # n1.insert(1000,n1.head)
# L = LinkedList()
# L.insert(10,L.head)
# print('List is: ')
# print(L)
# L.insert(12,L.head.next)
# print('List is: ')
# print(L)
# L.insert(2,L.head)
# print('List is: ')
# print(L)
# print('Size of L is ',L.len())
# L.delete(L.head)
# print('List is: ')
# print(L)
# L.delete(L.head.next)
# print('List is: ')
# print(L)
# print('List is empty?',L.isEmpty())
# print('Size of L is ',L.len())
# L.delete(L.head)
# print('List is empty?',L.isEmpty())
# print('Size of L is ',L.len())
# L.insertAtindex(2,0)
# L.insertAtindex(1,0)
# L.insertAtindex(4,2)
# L.insertAtindex(3,2)
# print('List is: ')
# print(L)

# # n1.insert(5,n1.head)
# # print('list is =')
# # n1.insert(12,n1.head.next)
# # n1.insert(69,n1.head.next)
# # n1.insert(45,n1.head)
# # n1.insert(8,n1.head.next)
# # n1.insert(123,n1.head)
# # n1.insert(6,n1.head)


