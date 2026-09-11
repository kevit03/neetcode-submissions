class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        counter = Counter(strs[i])
        hashmap = {}

        while i < len(strs): 
            counter = Counter(strs[i])
            key = tuple(sorted(counter.items()))
            if key not in hashmap:
                hashmap[key] = [strs[i]]
            elif key in hashmap:
                hashmap[key].append(strs[i])
            i+=1

        return list(hashmap.values())

        