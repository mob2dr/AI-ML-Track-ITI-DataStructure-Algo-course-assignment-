class Node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
       return self.data