# 알고리즘 수업
# 핵심 아이디어
# 1. tree 를 dictionary로 생성하고, root는 key로, left와 right는 value로 둔다.
# 2. 전위순회, 중위순회, 후위순회는 재귀함수를 이용한다.
import sys
input = sys.stdin.readline

tree_dict = {}

n=int(input())
for i in range(n):
    root, left, right = input().split()
    tree_dict[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(tree_dict[root][0])
        preorder(tree_dict[root][1])
def inorder(root):
    if root != '.':
        inorder(tree_dict[root][0])
        print(root, end="")
        inorder(tree_dict[root][1])
def postorder(root):
    if root != '.':
        postorder(tree_dict[root][0])
        postorder(tree_dict[root][1])
        print(root, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
