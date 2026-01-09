Opeartions:
1️⃣ insert_at_beggining(data)
Operation: Add a new node at the start of the list

2️⃣ insert_at_end(data)
Operation: Add a new node at the end of the list

3️⃣ insert_values(values)
Operation: Insert multiple values into the list

4️⃣ get_lentgh()
Operation: Count how many nodes are in the list

5️⃣ remove_at(index)
Operation: Delete the node at a specific position

6️⃣ insert_at(index, data)
Operation: Insert a value at a specific position

7️⃣ print_list()
Operation: Display all elements

+-------------------------------------------------------------+
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, values):
        self.head = None
        for data in values:
            self.insert_at_end(data)

    def get_lentgh(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def remove_at(self, index):
        if index < 0 or index >= self.get_lentgh():
            raise IndexError("index out of range")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_lentgh():
            raise IndexError("index out of range")

        if index == 0:
            self.insert_at_beggining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


# ---------------- TEST ----------------
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(['a', 'b', 'c', 'd'])

    ll.insert_at_beggining('z')   # z → a → b → c → d

    ll.remove_at(4)   # removes d
    ll.remove_at(3)   # removes c

    ll.insert_at(2,"figs")

    ll.print_list()
    print("length of list:", ll.get_lentgh())
