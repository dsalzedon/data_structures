from typing import Any, Optional

from helpers.node import NodeHelper


class LinkedList:
    def __init__(self, value: Any):
        """Init."""
        new_node = NodeHelper(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value: Any) -> bool:
        """Create new node and add it to the end.

        0(1)

        Args:
            value: value to store in the node.
        """
        new_node = NodeHelper(value=value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def get(self, index: int) -> Optional[NodeHelper]:
        """Return node for the given index.

        O(n)

        Args:
            index: index of the node.
        """
        if index < 0 or index >= self.length:
            return None

        temp_value = self.head
        for _ in range(index):
            temp_value = temp_value.next

        return temp_value

    def insert(self, index: int, value: Any) -> bool:
        """Create new node and insert node to given index.

        O(n)

        Args:
            index: index to insert node.
            value: value to store in the node.
        """
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.prepend(value=value)
        elif index == self.length:
            return self.append(value=value)

        new_node = NodeHelper(value=value)

        before_node = self.get(index=index-1)

        new_node.next = before_node.next

        before_node.next = new_node

        self.length += 1

        return True

    def pop(self) -> Optional[NodeHelper]:
        """Remove last node.

        O(n)
        """
        if not self.length:
            return None

        temp_value = self.head
        pre_value = self.head

        while temp_value.next:
            pre_value = temp_value
            temp_value = temp_value.next

        self.tail = pre_value
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp_value

    def pop_first(self):
        """Remove first node of the list.

        O(1)
        """
        if not self.length:
            return None

        temp_value = self.head
        self.head = self.head.next
        temp_value.next = None
        self.length -= 1

        if not self.length:
            self.tail = None

        return temp_value

    def prepend(self, value: Any) -> bool:
        """Create new node and add it to beginning.

        O(1)
        Args:
            value: value to store in the node.
        """
        new_node = NodeHelper(value=value)

        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def print_list_values(self):
        """Print all elements in the LinkedList."""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def print_list_attributes(self):
        """Print all attributes of the LinkedList."""
        print('Head:', self.head.value)
        print('Tail:', self.tail.value)
        print('Length:', self.length)

    def set_value(self, index: int, value: Any) -> bool:
        """Create new node and insert node.

        O(n)
        Args:
            index: index to insert node.
            value: value to store in the node.
        """
        temp_value = self.get(index=index)

        if not temp_value:
            return False

        temp_value.value = value

        return True

    def remove(self, index: int) -> Optional[bool]:
        """Remove node from given index.

        O(n)
        Args:
            index: index to remove node.
        """
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()

        previous_node = self.get(index=index-1)
        temp = previous_node.next
        previous_node.next = temp.next
        temp.next = None
        self.length -= 1
        return True

    def reverse(self) -> Optional[bool]:
        """Reverse the linked list.

        O(n)
        """
        temp_value = self.head
        self.head = self.tail
        after = temp_value.next
        before = None

        for _ in range(self.length):
            after = temp_value.next
            temp_value.next = before
            before = temp_value
            temp_value = after

        return True
