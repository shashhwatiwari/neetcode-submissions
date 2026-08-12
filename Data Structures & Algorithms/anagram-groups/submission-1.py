class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortWord(char):
            word = "".join(sorted(char))
            return word
        lib = {}
        for word in strs:
            sortedWord = sortWord(word)
            if sortedWord in lib:
                continue
            else:
                lib[sortedWord] = []
        for word in strs:
            sortedWord = sortWord(word)
            lib[sortedWord].append(word)
        return list(lib.values())


                
                

        