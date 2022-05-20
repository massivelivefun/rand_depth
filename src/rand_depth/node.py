from typing import Generic, TypeVar

T = TypeVar('T')  # pragma: no mutate


class Node(Generic[T]):
    def __init__(self, contents: T, left: 'Node[T]', right: 'Node[T]'):
        self.contents = contents  # pragma: no mutate
        self.left = left  # pragma: no mutate
        self.right = right  # pragma: no mutate
