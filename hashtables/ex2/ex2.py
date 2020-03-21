#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #Let's Hash things using the "source", which is really origin, and destination
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    # Iterate through the tickets matching the destination 
    # of the current value with the starting point of the next (finding the link in the chain)

    current_val = hash_table_retrieve(hashtable, "NONE")

    route[0] = current_val
    
    for i in range(1, length):
        next_val = hash_table_retrieve(hashtable, current_val)
        route[i] = next_val
        current_val = next_val
    return route[:-1]
