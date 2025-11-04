# Explanation of Top K Frequent Elements (Bucket Sort Method)

1. We need to find the k most frequent numbers in an array.

2. count = {}
   - Use a dictionary to count how many times each number appears.

3. freq = [[] for i in range(len(nums) + 1)]
   - Create a list of empty lists (buckets).
   - Index i represents all numbers that appear i times.

4. for n in nums:
       count[n] = 1 + count.get(n, 0)
   - Build the frequency map.

5. for n, c in count.items():
       freq[c].append(n)
   - Place each number into its corresponding frequency bucket.

6. res = []
   for i in range(len(freq) - 1, 0, -1):
       for n in freq[i]:
           res.append(n)
           if len(res) == k:
               return res
   - Iterate backwards through buckets (highest frequency first).
   - Add numbers to the result until we have k of them.

7. Return res as the list of top k frequent numbers.

# Example:
# nums = [1,1,1,2,2,3], k = 2
# count = {1:3, 2:2, 3:1}
# freq = [[], [3], [2], [1], [], [], []]
# Output: [1, 2]
