class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def set_node(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def set_right(self, data):
        self.right = Tree(data)

    def set_left(self, data):
        self.left = Tree(data)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(" node : ", self.data)
        if self.right:
            self.right.PrintTree()

    def __repr__(self):
        return str(self.data)