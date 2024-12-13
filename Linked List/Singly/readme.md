# **Singly Linked List**

## **What is a Linked List?**
A linked list is a fundamental data structure made up of nodes. Each node contains:
- **Data**: The value stored in the node.
- **Next**: A reference (or pointer) to the next node in the list.

The last node’s `next` is `null`, indicating the end of the list.

---

## **Node Structure**
![image](https://github.com/user-attachments/assets/967392e5-971e-4249-aa42-7925b72b8c6b)

---

## **Operations on Singly Linked List**
### **1. Traversal**
Move through each node in the list to access or display its data.

### **2. Searching**
Find a specific value in the list by traversing node by node.

### **3. Length**
Count the total number of nodes in the list.

### **4. Insertion**
You can insert nodes into a singly linked list in three ways:
- **At the beginning**
- **At the end**
- **At a specific position**

### **5. Deletion**
You can delete nodes from a singly linked list in three ways:
- **From the beginning**
- **From the end**
- **A specific node**

---

## **Insertion Operations**

### **Insert at the Beginning**
1. Create a new node with the given value.
2. Set the new node’s `next` to the current head.
3. Update the head to point to the new node.

---

### **Insert at the End**
1. Create a new node with the given value.
2. If the list is empty, set the new node as the head.
3. Otherwise, traverse the list to the last node.
4. Set the last node’s `next` to the new node.

---

## **Deletion Operations**

### **Delete from the Beginning**
1. Check if the list is empty (head is `null`). If it is, return `null`.
2. Move the head pointer to the next node.
3. Delete the old head node.

---

### **Delete from the End**
1. Check if the list is empty (head is `null`). If it is, return `null`.
2. If there is only one node, delete the head and return `null`.
3. Otherwise, traverse to the second-to-last node.
4. Delete the last node and set the second-to-last node’s `next` to `null`.

