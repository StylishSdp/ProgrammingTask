class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTree:
    def __init__(self, node_list):
        self.root = node_list[0]
        for i in node_list[1:]:
            self.insert(i)

    def search(self, node, parent, val):
        if node is None:
            return False, node, parent
        if node.val == val:
            return True, node, parent
        if node.val > val:
            self.search(node.left, parent, val)
        else:
            self.search(node.right, parent, val)

    def insert(self, val):
        flag, node, parent = self.search(self.root, self.root, val)
        if not flag:
            new_node = TreeNode(val)
            if val > parent.val:
                parent.right = new_node
            else:
                parent.left = new_node

    def delete(self, root, val):
        flag, node, parent = self.search(root, root, val)
        if not flag:
            print('No searching')
            return
        else:
            if node.left is None and node.right is None:
                del node
            elif node.left is None:
                if node == parent.right:
                    parent.right = node.right
                else:
                    parent.right = node.right
                del node
            elif node.right is None:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
                del node
            else:
                #node的左右子树均不为空
                #寻找中序立即后继者  从node的右子树开始，往左找
                temp = node.right
                if temp.left is None:
                    node.val = temp.val
                    node.right = temp.right
                    del temp
                else:
                    next = temp.left
                    while next.left is not None:  #一直向左寻找左孩子，
                        temp = next
                        next = next.left
                    node.val = next.val       #删除找到的最后一个左孩子
                    temp.left = next.right
                    del next

    def preorder(self, node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)


    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def inorderTraversal(self, root):
        # 非递归
        # 有左儿子，则自己入栈，r = r.left
        # 栈顶(自己)被弹出，访问自己，r = r.right
        r = root
        stack = []
        res = []
        while (stack or r):
            while (r):
                stack.append(r)
                r = r.left
            if (stack):
                r = stack[-1]
                res.append(r.val)
                stack.pop()
                r = r.right
        return res


    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)

    # 后序打印二叉树（非递归）
    # 使用两个栈结构
    # 第一个栈进栈顺序：左节点->右节点->跟节点
    # 第一个栈弹出顺序： 跟节点->右节点->左节点(先序遍历栈弹出顺序：跟->左->右)
    # 第二个栈存储为第一个栈的每个弹出依次进栈
    # 最后第二个栈依次出栈
    def postOrderTraverse(self,node):
        stack = [node]
        stack2 = []
        while len(stack) > 0:
            node = stack.pop()
            stack2.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        while len(stack2) > 0:
            print(stack2.pop().val)
    def levelorder(self, root):
        #使用队列，父节点出队，左右孩子入队
        queue = [root]
        res = []
        while queue and root:
            res.append(queue[0].val)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)
        return res

