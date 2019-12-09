from typing import Tuple
import numpy as np
import string


class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def make_alpahbetList(self):
        for l in list(string.ascii_lowercase):
            newNode = Node(l, self.head)
            self.head = newNode
            self.size += 1

    def getSize(self):
        return self.size

    def addNode(self, data):
        curr = self.head
        while curr:
            if curr.getData() == data:
                return False, "already in the list"
            curr = curr.getNextNode()

        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True, "Added to the list"

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()

    def removeNode(self, value):

        prev = None
        curr = self.head
        while curr:
            if curr.getData() == value:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True

            prev = curr
            curr = curr.getNextNode()
        return False

    def findNode(self, value):
        curr = self.head
        while curr:
            if curr.getData() == value:
                return True
            curr = curr.getNextNode()
        return False

    def get_list(self):
        curr = self.head
        all_list = []
        while curr:
            all_list.append(curr.getData())
            curr = curr.getNextNode()
        return all_list


class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    counter = 0

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1


def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                print("character is : ", char)
                print("node.child is :", child.char)
                print(child.char == char)
                print("\n")
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                # And point the node to the child that contains this char

                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node

    if found_in_child:
        node.counter = node.counter + 1

    # Everything finished. Mark it as the end of a word.
    # node.counter += 1
    node.word_finished = True


def _add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('*')
    # add(root, "hackathon")
    # add(root, 'hack')

    # str ="royaisniceroyaisperfectroyaaroya"
    str = "aababca"
    index = 3

    for i in range(index):
        # print(i,"-",index)
        substr = str[i:index]
        print(substr)
        _add(root, substr)

    print("************************************")
    for j in range(index, len(str)):
        # print("j-index+1 = ",j-index+1,"j+index = ",j+1)
        # print(str[ j-index+1: j+1])
        for k in range(index):
            # print("j-index+1 = ", j -index + 1 +k , "j+index = ", j + 1)
            # print(str[j - index + 1 +k : j + 1])
            substr = str[j - index + 1 + k: j + 1]
            print(substr)
            add(root, substr)
            # add(root, substr)

    myList = LinkedList()
    myList.make_alpahbetList()
    # myList.printNode()
    print(myList.get_list())

    j = len(str) - index + 1
    max = -1
    str_max = ""
    candid = []

    list_iter = myList.get_list();
    print("list iteration is ",list_iter)
    while j < len(str) :
        candid = []
        print("j is : ", j, " candid is :", candid)
        f = 0
        # print(str[j:len(str)])

        for i in list_iter:
            # print(str[j:len(str)]+ i, find_prefix(root,str[j:len(str)]+ i ))
            in_list, weight = find_prefix(root, str[j:len(str)] + i)
            # print(str[j:len(str)]+ i , weight)

            if weight == max:
                print(str[j:len(str)] + i, weight)
                f = f + 1
                candid.append(i)
            if max < weight:
                print(str[j:len(str)] + i, weight)
                f = 1
                str_max = str[j:len(str)] + i
                max = weight
                candid = []
                candid.append(i)

        print("J is : ", str[j])
        myList.removeNode(str[j])
        myList.addNode(str[j])

        print("j is : ", j, " candid is :", candid[0])

        # print(f)
        if f == 1: # age candid 1 item dasht
            print("F is ", f)
            j = j + 1
            while j < len(str):
                print("J is : ", str[j])
                myList.removeNode(str[j])
                myList.addNode(str[j])
                j = j + 1
            print(" i is : ", candid[0])
            myList.removeNode(candid[0])
            myList.addNode(candid[0])
            candid = []
            break

        #candid = []
        j = j + 1
    for candids in candid:
        print(" i is : ", candids)
        myList.removeNode(candids)
        myList.addNode(candids)
    print("Hiiiiiiiiiiiiiii")
    print("list iteration is ", list_iter)
    # bring to the front
    #myList.removeNode(candid)
    #myList.addNode(candid)

    print("******************************")
    myList.printNode()



