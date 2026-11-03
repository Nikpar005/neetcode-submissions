from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        folders = defaultdict(list)

        for word in strs:
            folder_name = tuple(sorted(word))

            folders[folder_name].append(word)
        return list(folders.values())