word = input()
n = [0] * len(word)  

for i in range(len(word)): # 한글자를
    for x in range(65,91) : # 알파벳 이랑 비교하면서 
        if (chr(x) == word[i] and chr(x) == 'A') or (chr(x) == word[i] and chr(x) == 'B') or (chr(x) == word[i] and chr(x) == 'C'): # 같은게 있으면
            n[i] += 2 # n[i]에 수치만큼 더해주기 
        elif (chr(x) == word[i] and chr(x) == 'D') or (chr(x) == word[i] and chr(x) == 'E')or (chr(x) == word[i] and chr(x) == 'F'): 
            n[i] += 3 
        elif (chr(x) == word[i] and chr(x) == 'G') or (chr(x) == word[i] and chr(x) == 'H') or (chr(x) == word[i] and chr(x) == 'I'): 
            n[i] += 4
        elif (chr(x) == word[i] and chr(x) == 'J') or (chr(x) == word[i] and chr(x) == 'K') or  (chr(x) == word[i] and chr(x) == 'L'): 
            n[i] += 5 
        elif (chr(x) == word[i] and chr(x) == 'M') or (chr(x) == word[i] and chr(x) == 'N') or  (chr(x) == word[i] and chr(x) == 'O'): 
            n[i] += 6 
        elif (chr(x) == word[i] and chr(x) == 'P') or (chr(x) == word[i] and chr(x) == 'Q') or  (chr(x) == word[i] and chr(x) == 'R') or (chr(x) == word[i] and chr(x) == 'S'): 
            n[i] += 7 
        elif (chr(x) == word[i] and chr(x) == 'T') or (chr(x) == word[i] and chr(x) == 'U') or (chr(x) == word[i] and chr(x) == 'V'): 
            n[i] += 8
        elif (chr(x) == word[i] and chr(x) == 'W') or (chr(x) == word[i] and chr(x) == 'X') or  (chr(x) == word[i] and chr(x) == 'Y') or (chr(x) == word[i] and chr(x) == 'Z'): 
            n[i] += 9 

Hap = 0
for i in n:
    Hap += i
print(Hap + len(n))

        
        
