class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        merge = ''

        len_word1 = len(word1)
        len_word2 = len(word2)

        shorter_len = len_word1 if len_word1 <= len_word2 else len_word2

        for i in range(shorter_len):
            merge += word1[i] + word2[i]
        
        if len_word1 > shorter_len:
            merge += word1[shorter_len:]
        elif len_word2 > shorter_len:
            merge += word2[shorter_len:]

        return merge
