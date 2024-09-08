#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s.split(): 各単語を要素とするリストを返す。
        # filter関数は、第1引数に条件（ラムダ関数）を、第2引数にリストを取る。
        words = filter(lambda word: word != "", s.split(" "))

        # reduce関数は、第1引数に2つの引数を取る関数、第2引数にイテラブルを取る。
        # ラムダ関数の引数_には前回の累積結果が渡されますが、今回は累積値を無視して、
        # 常に最新のwordを返します。このようにして、最終的に最後の単語が得られます。
        # なぜなら、lambda関数が実行される度、後続のwordで上書き（再代入）されるから。
        return len(reduce(lambda _, word: word, words))

        # words = []
        # word = ""

        # for char in s:
        #     if char == " ":
        #         if word:
        #             words.append(word)
        #             word = ""
        #     elif char == s[-1]:
        #         word += char
        #         words.append(word)

        #     else:
        #         word += char
        
        # return len(words[-1])


        # @lc code=end

