class leetcode:
    def sliding_window(self, nums, k):
        n = len(nums)

        # Step 1: first window
        sums = 0
        for i in range(k):
            sums += nums[i]

        maxx = sums

        # Step 2: sliding window
        for i in range(k, n):
            sums = sums + nums[i] - nums[i - k]

            if sums > maxx:
                maxx = sums

        return maxx


nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

leetcode1 = leetcode()
print(leetcode1.sliding_window(nums, k))
