"""Node to be exported"""

from typing import Any

class Node:
    """ Create Node """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
