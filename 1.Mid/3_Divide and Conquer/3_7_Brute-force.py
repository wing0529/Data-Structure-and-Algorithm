
#brute-force 

def bit_str(ans):# ans은 local variable
    if len(ans)==n:
        print(*ans)
    else:
        for s in data:
            ans.append(s) #ans에 값 추가 됨 
            bit_str(ans)
            ans.pop()

n,data=3,'abc' # global variable
bit_str([])

''' DFS(Deapth Fast Search)

🎯 Level 0:
ans = []   → append 'a' → ['a']  

🎯 Level 1:
ans = ['a']  → append 'a' → ['a', 'a']  

🎯 Level 2:
ans = ['a', 'a']  
  → append 'a' → ['a', 'a', 'a'] 
  ✅ 출력: `a a a`  
  → pop() → ['a', 'a']

  → append 'b' → ['a', 'a', 'b']  
  ✅ 출력: `a a b`  
  → pop() → `['a', 'a']`

  → append `'c'` → `['a', 'a', 'c']`  
  ✅ 출력: `a a c`  
  → pop() → `['a', 'a']`

  → pop() → `['a']` (Level 1로 복귀!)

🎯 Level 1 다시:
  → append `'b'` → `['a', 'b']`  

🎯 Level 2:
  → append `'a'` → `['a', 'b', 'a']`  
  ✅ 출력: `a b a`  
  → pop() → `['a', 'b']`

  → append `'b'` → `['a', 'b', 'b']`  
  ✅ 출력: `a b b`  
  → pop() → `['a', 'b']`

  → append `'c'` → `['a', 'b', 'c']`  
  ✅ 출력: `a b c`  
  → pop() → `['a', 'b']`

  → pop() → `['a']`

🎯 Level 1 다시:
  → append `'c'` → `['a', 'c']`  


'''