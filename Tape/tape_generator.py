# The set of pages that remains in memory at runtime depends on three factors: the prefetching algorithm, the eviction
# policy, and the amount of available local memory. Thus to generate a tape, 3PO’s post-processor traverses the trace, simulating 3PO’s perfect prefetching algorithm and an eviction policy
# with a particular target local memory size to determine which
# pages will not be present and will need to be prefetched. Ideally 3PO would simulate Linux’s eviction policy, since this is
# what will be used at runtime. Unfortunately, Linux’s eviction
# policy is quite complex and depends on the timing of different
# events [ 13], so it would be difficult to simulate it accurately.
# Instead, 3PO simulates a simple LRU eviction policy. Linux’s
# eviction policy bears some resemblance to LRU but differs in
# many ways; despite this we found that simulating LRU instead
# is accurate enough to avoid major page faults in practice (§5.5).

class Node:
    def __init__(self, key):
        self.key = key
        # self.value = value
        self.prev = None
        self.next = None

class LRU_Dram:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ram = {}
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node):
        """Add new node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node: Node):
        """Move certain node to head."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Pop the current tail."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.ram.get(key, None)
        if not node:
            return -1
        # Move the accessed node to the head;
        self._move_to_head(node)
        return 1

    def contains(self, key: int) -> bool:
        node = self.ram.get(key, None)
        if not node:
            return False
        # Move the accessed node to the head;
        return True

    def put(self, key: int) -> None:
        node = self.ram.get(key)
        if not node:
            new_node = Node(key)
            self.ram[key] = new_node
            self._add_node(new_node)
            if len(self.ram) > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.ram[tail.key]
        else:
            # Update the value.
            # node.value = value
            self._move_to_head(node)


class PerfectPrefetcher:
    def __init__(self, ram_size):
        self.ram_size = ram_size
        self.ram = LRU_Dram(ram_size)
        self.future_accesses = []
    
    def prefetch(self, address):
        self.ram.put(address)
        print(f"Prefetched address: {address}")

    def access(self, address):
        # Simulate perfect prefetching
        if self.future_accesses:
            next_address = self.future_accesses.pop(0)
            self.prefetch(next_address)
        
        if self.ram.contains(address):
            print(f"Accessing address: {address} (hit)")
        else:
            print(f"Accessing address: {address} (miss)")

    def simulate(self, access_sequence):
        # Load the future accesses
        self.future_accesses = access_sequence.copy()
        for address in access_sequence:
            self.access(address)

# Example usage
ram = LRU_Dram(2)
ram.put(1)
ram.put(2)
print(ram.get(1))    # returns 1
ram.put(3)        # evicts key 2
print(ram.get(2))    # returns -1 (not found)
ram.put(4)        # evicts key 1
print(ram.get(1))    # returns -1 (not found)
print(ram.get(3))    # returns 3
print(ram.get(4))    # returns 4

ram_size = 4
disk_size = 1000
access_sequence = [100, 200, 300, 400, 100, 500, 200, 600, 300, 700]

prefetcher = PerfectPrefetcher(ram_size)
prefetcher.simulate(access_sequence)