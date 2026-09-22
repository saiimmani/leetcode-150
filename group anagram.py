class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        groups = {}

        for word in strs:
            key = "".join(sorted(word)) #  Example Stores Key -> "aet"
            # Sorted(word) -> eat -> 'a' , 'e' , 't'
            
            if key not in groups:
                groups[key] = []    # if aet is not in dic we create list 
            
            groups[key].append(word)  # Add to Key ->  { "aet": ["eat"] }

        return list(groups.values())
