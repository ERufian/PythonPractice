class Solution(object):
    def threeSum(self, nums):
        # Build dictionary of val => list of indices
        ix_from_val = {}
        for i in range(len(nums)):
            ix_from_val[nums[i]] = [i] if nums[i] not in ix_from_val else ix_from_val[nums[i]] + [i]
        # nested loops of unique keys to build all pairs
        sumsets = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # for each pair, check whether required number is in table
                twosum = nums[i] + nums[j]
                if -twosum in ix_from_val:
                    # add it only if not a permutation of previous
                    last_ix = ix_from_val[-twosum][-1]
                    if last_ix > j:
                        sumsets.add(tuple(sorted([nums[i], nums[j], nums[last_ix]])))
        r = []
        for s in sumsets:
            r.append(list(s))
        return r
