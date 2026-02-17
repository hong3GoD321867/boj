#boj 6996번 애너그램
N=int(input())
for _ in range(N):
    word,word1=list(map(str,input().split()))
    nword=sorted(word)
    nword1=sorted(word1)
    if nword==nword1:
        print(f"{word} & {word1} are anagrams.")
    else:
        print(f"{word} & {word1} are NOT anagrams.")

