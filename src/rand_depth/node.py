from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, contents: None, left: 'Node[T]', right: 'Node[T]'):
        self.contents = contents
        self.left = left
        self.right = right
