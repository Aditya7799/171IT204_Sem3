class List_Node:

    def __init__(self,a):
        self.value=a
        self.next=None

    



class LinkedList:

    def __init__(self,h):
        self.head=h


    def __init__(self):
        self.head=None
        


    def insertAtIndex(self,index,val):
        curr=self.head
        i=1

        if(index==0 and not(self.isEmpty())):
            temp=List_Node(val)
            temp.next=self.head
            self.head=temp
            return


        if(self.isEmpty() and index==0):
            temp=List_Node(val)
            self.head=temp
            return



        while(curr!=None):
            if(i==index):
                temp=List_Node(val)
                temp.next=curr.next
                curr.next=temp
                break
            i=i+1
            curr=curr.next

        if(curr==None):
             print("Cannot insert ",str(val)," at Given Index")

       

    def deleteAtIndex(self,index):
        x=0
        curr=self.head
        i=1
        if(index==0):
            self.head=curr.next
            return



        while(curr!=None):
            if(i==index):
                x=curr.next.value
                curr.next=curr.next.next
                return x

            i=i+1
            curr=curr.next
        print("Cannot Delete at given index")
        return None





    def search(self,value):
        curr=self.head
        i=0;
        while(curr!=None):
            if(curr.value==value):
                return i
            curr=curr.next
            i=i+1

        print("Element not found")
        return None




    def __str__(self):
        a=""
        curr=self.head
        while(curr!=None):
            a=a+" "+(str(curr.value))
            curr=curr.next
        return a



    def search(self,element):
        curr=self.head
        i=0
        while(curr!=None):
            if(curr.value==element):
                return i
            i=i+1
            curr=curr.next
        return None


    def Length(self):
        curr=self.head
        len=0
        while(curr!=None):
            curr=curr.next
            len=len+1
        return len

    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False








def main():
    
    L=LinkedList()

    b=False

    while(not(b)):
        print("Enter Choice:","1.Insert","2.Delete","3.Search","4.End",sep="\n",end="\n")
        x=int(input())

        if(x==1):
            print('Enter Element and index to be inserted at')
            ele=int(input())
            index=int(input())
            print("Before inserting",L)
            L.insertAtIndex(index,ele)
            print("After Inserting",L)

        elif(x==2):
            print('Enter index to be deleted')
            index=int(input())
            print("Before deleting",L)
            L.deleteAtIndex(index)
            print("After Deleting",L)


        elif(x==3):
            print('Enter Element to be searched for')
            ele=int(input())
            a=L.search(ele)
            if(x!=None):
                print("Found at ",str(a))
            else:
                print("NOt found")

        elif(x==4):
            b=True












    
    print(L)






main()


























                


