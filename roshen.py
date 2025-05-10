# Ordinary chocolate bar n x m
class Chocolate():
    def __init__(self, n, m, size=None):
        self.n = n
        self.m = m

        if size == None:
            self.size = n * m
        else:
            self.size = size

        self.left = None
        self.right = None

    # def divide(self, direction, position):
    def divide(self):
        if self.n > 1:
            return (Chocolate(self.n - 1, self.m), Chocolate(1, self.m))
        elif self.m > 1:
            return (Chocolate(self.n, self.m - 1), Chocolate(self.n, 1))

        raise Exception("Cannot divide single chocolate square...")

    def __str__(self):
        return f"chocolate piece {self.n}x{self.m}"

    def __repr__(self):
        if not self.left and not self.right:
            return f"piece {self.n}x{self.m}"

        if self.left and self.right:
            return f"{self.__str__()}\n\t"

        if self.left or self.right:
            if self.left:
                return f"piece {self.n}x{self.m}\n\t{self.left.__str__()}"
            else:
                return f"piece {self.n}x{self.m}\n\t{self.right.__str__()}"

# until all chocolate divided to squares 1x1
def build_chocolate_tree(root: Chocolate):
    if root.size <= 1: return

    root.left, root.right = root.divide()
    # print(f"\t{root.left.n, root.left.m} | {root.right.n, root.right.m}")

    build_chocolate_tree(root.left)
    build_chocolate_tree(root.right)

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

if __name__ == "__main__":
    root = Chocolate(6,3)
    build_chocolate_tree(root)
