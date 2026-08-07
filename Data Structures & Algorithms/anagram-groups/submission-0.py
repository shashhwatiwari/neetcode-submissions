class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def makeWord(wordList):
            word = "".join(sorted(wordList))
            return word

        wordDict = {}
        for let in strs:
            sortedLet = makeWord(let)
            if sortedLet in wordDict:
                continue
            else:
                wordDict[sortedLet] = []
        
        for let in strs:
            tempWord = makeWord(let)
            if tempWord in wordDict:
                wordDict[tempWord].append(let)

        return list(wordDict.values()) 
        
        

                
                

        