# A program that prints the longest substring of s 
# in which the letters occur in alphabetical order

arr = []
ans = ''
s = "abcbbcgfafgsagasdavbdnhdhd"
for letter in s:
        if ans == '':
                ans += letter
        else:
                if ans[-1] <= letter:
                        ans += letter
                else:
                        arr.append(ans)
                        ans = letter
arr.append(ans)
 
longest_sub = ''
 
for string in arr:
        if len(string) > len(longest_sub):
                longest_sub = string
 
print longest_sub