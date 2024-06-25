class PerfectPrefetcher:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = set()
        self.future_accesses = []
    
    def prefetch(self, address):
        if address not in self.cache:
            if len(self.cache) >= self.cache_size:
                # Evict the least recently used item, which in this case is straightforward
                # because we are prefetching perfectly based on future accesses.
                self.cache.pop()
            self.cache.add(address)
        print(f"Prefetched address: {address}")

    def access(self, address):
        # Simulate perfect prefetching
        if self.future_accesses:
            next_address = self.future_accesses.pop(0)
            self.prefetch(next_address)
        
        if address in self.cache:
            print(f"Accessing address: {address} (cache hit)")
        else:
            print(f"Accessing address: {address} (cache miss)")

    def simulate(self, access_sequence):
        # Load the future accesses
        self.future_accesses = access_sequence.copy()
        for address in access_sequence:
            self.access(address)

# Example usage
cache_size = 4
access_sequence = [100, 200, 300, 400, 100, 500, 200, 600, 300, 700]

prefetcher = PerfectPrefetcher(cache_size)
prefetcher.simulate(access_sequence)