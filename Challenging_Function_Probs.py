### 007 Game ###

def spy_game(nums):

  code = [0,0,7,'x']
  
  for i in nums:
    if num == code[0]:
      code.pop(0)
      
  return len(code) == 1


---------------------------------------------------------


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in range(3,x,2):  # test all odd factors up to x-1
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


---------------------------------------------------------



def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
        
        
        
--------------------------------------------------

### Summer 69 ###

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total
    
#OR

def summer_69(arr):
    
    total = 0
    add = True
    
    for num in arr:
        if add:
            if num != 6:
                total += num
            else:
                add = False
        else:
            if num == 9:
                add = True
    return total
    
    
#The second way is better one since in professional people tend to use while loop for something they do not want to stop 
#until they get the outcome they want or til the condition is met and return some value or simply print something out. 
-----------------------------------------------

 def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]