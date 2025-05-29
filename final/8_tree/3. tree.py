import sys
sys.stdin=open('tree1.txt','r')

n = int(input())

tree ={}
root = 'A'
for _ in range(n):
    parent, left, right = input().split()
    tree[parent]=[left,right]

def inorder(node):
    if node != '-':
        inorder(tree[node][0])
        print(node,end=' ')
        inorder(tree[node][1])

def preorder(node):
    if node != '-':
        print(node,end=' ')
        inorder(tree[node][0])
        inorder(tree[node][1])


def postorder(node):
    if node != '-':
        inorder(tree[node][0])
        inorder(tree[node][1])
        print(node,end=' ')


print("inorder : ")
inorder(root)
print("\npreorder : ")
preorder(root)
print("\npostorder : ")
postorder(root)