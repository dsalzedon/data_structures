from data_structures.linked_list import LinkedList


def linked_list():
    """Linked List."""
    my_linked_list = LinkedList(value=4)

    my_linked_list.append(value=5)

    my_linked_list.append(value=10)
    my_linked_list.append(value=3)
    my_linked_list.append(value=2)

    my_linked_list.insert(index=1, value=8)
    my_linked_list.remove(index=2)

    my_linked_list.print_list_values()
    my_linked_list.reverse()
    my_linked_list.print_list_values()

