import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_list = []
        heapq.heapify(nums)
        for val in nums:
            heapq.heappush(self.sorted_list, val)

    def add(self, val: int) -> int:
        heapq.heappush(self.sorted_list, val)
        while len(self.sorted_list) > self.k:
            heapq.heappop(self.sorted_list)
        return self.sorted_list[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)