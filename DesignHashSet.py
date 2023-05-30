class MyHashSet:

    def __init__(self, size=512):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        bucket = key % self.size
        if key not in self.buckets[bucket]:
            self.buckets[bucket].append(key)
        return

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.size]
        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
        return

    def contains(self, key: int) -> bool:
        bucket = key % self.size
        return key in self.buckets[bucket]
