class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if not text1 or not text2:
        #     return 0
        # if text1[-1] == text2[-1]:
        #     return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        # else:
        #     return max(self.longestCommonSubsequence(text1, text2[:-1]), self.longestCommonSubsequence(text1[:-1], text2))
        memo = {}
        def memoisedLCS(str1, str2, indx1, indx2):
            if indx1 < 0 or indx2 < 0:
                return 0
            elif (indx1,indx2) in memo:
                return memo[(indx1,indx2)]
            else:
                if str1[indx1] == str2[indx2]:
                    memo[(indx1,indx2)] = 1 + memoisedLCS(str1, str2, indx1-1, indx2-1)
                else:
                    memo[(indx1,indx2)] = max(memoisedLCS(str1, str2, indx1-1, indx2), memoisedLCS(str1, str2, indx1, indx2-1))
                return memo[(indx1,indx2)]

        len1 = len(text1) - 1
        len2 = len(text2) - 1
        return memoisedLCS(text1, text2, len1, len2)
        