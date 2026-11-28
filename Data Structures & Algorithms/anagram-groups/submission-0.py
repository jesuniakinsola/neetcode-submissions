class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      groups = {}
         
        # sorted word -> list of original words
      
      for word in strs:    # values are enough; no index needed
        key = "".join(sorted(word))        # sorted version of word

        if key not in groups:
            groups[key] = []# start an empty list for a new group

        groups[key].append(word)    # add word to its group's list
        
      return list(groups.values())     # all the lists