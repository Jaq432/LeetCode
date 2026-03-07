# def longestPalindrome(s: str) -> str:
#     if len(s) == 0:
#         return ""
#     if len(s) == 1:
#         return s
#     palindromeSubstrings = []
    
#     # Get all of the palindrome strings
#     # Iterate forward for each letter
#     for k,i in enumerate(s):
#         # Iterate backward for each letter
#         for j,l in enumerate(s[k:]):
#             #print(s[k:len(s)-j])
#             if s[k:len(s)-j] == s[k:len(s)-j][::-1]:
#                 palindromeSubstrings.append(s[k:len(s)-j])
#     #print(palindromeSubstrings)
#     longestSubstring = ""
#     longestSubstringLength = 0
#     for i in palindromeSubstrings:
#         if len(i) > longestSubstringLength:
#             longestSubstring = i
#             longestSubstringLength = len(i)

#     return longestSubstring

def longestPalindrome(s: str) -> str:
    if len(s) < 2:
        return s

    start = 0
    end = 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)       # odd length
        l2, r2 = expand(i, i + 1)   # even length

        if r1 - l1 > end - start:
            start, end = l1, r1

        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end+1]

#print(longestPalindrome("babad")) # bab or aba
#print(longestPalindrome("cbbd"))  # bb
#print(longestPalindrome("bb"))  # bb
#print(longestPalindrome("abcdefghijklmnopqrstuvwxyz"))
print(longestPalindrome("reifadyqgztixemwswtccodfnchcovrmiooffbbijkecuvlvukecutasfxqcqygltrogrdxlrslbnzktlanycgtniprjlospzhhgdrqcwlukbpsrumxguskubokxcmswjnssbkutdhppsdckuckcbwbxpmcmdicfjxaanoxndlfpqwneytatcbyjmimyawevmgirunvmdvxwdjbiqszwhfhjmrpexfwrbzkipxfowcbqjckaotmmgkrbjvhihgwuszdrdiijkgjoljjdubcbowvxslctleblfmdzmvdkqdxtiylabrwaccikkpnpsgcotxoggdydqnuogmxttcycjorzrtwtcchxrbbknfmxnonbhgbjjypqhbftceduxgrnaswtbytrhuiqnxkivevhprcvhggugrmmxolvfzwadlnzdwbtqbaveoongezoymdrhywxcxvggsewsxckucmncbrljskgsgtehortuvbtrsfisyewchxlmxqccoplhlzwutoqoctgfnrzhqctxaqacmirrqdwsbdpqttmyrmxxawgtjzqjgffqwlxqxwxrkgtzqkgdulbxmfcvxcwoswystiyittdjaqvaijwscqobqlhskhvoktksvmguzfankdigqlegrxxqpoitdtykfltohnzrcgmlnhddcfmawiriiiblwrttveedkxzzagdzpwvriuctvtrvdpqzcdnrkgcnpwjlraaaaskgguxzljktqvzzmruqqslutiipladbcxdwxhmvevsjrdkhdpxcyjkidkoznuagshnvccnkyeflpyjzlcbmhbytxnfzcrnmkyknbmtzwtaceajmnuyjblmdlbjdjxctvqcoqkbaszvrqvjgzdqpvmucerumskjrwhywjkwgligkectzboqbanrsvynxscpxqxtqhthdytfvhzjdcxgckvgfbldsfzxqdozxicrwqyprgnadfxsionkzzegmeynye"))