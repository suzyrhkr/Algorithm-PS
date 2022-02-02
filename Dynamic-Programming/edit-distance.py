class Solution(object):
    def minDistance(self, word1, word2):
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[0]*(len_word2+1) for _ in range(len_word1+1)]
 
        for i in range(1, len_word1+1):
            dp[i][0] = i
        for i in range(1, len_word2+1):
            dp[0][i] = i
        
        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    
        return dp[-1][-1]
                    