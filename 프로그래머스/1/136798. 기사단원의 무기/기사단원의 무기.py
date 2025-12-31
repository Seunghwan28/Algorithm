
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2   
            if i * i == n:
                count -= 1
    return count

def solution(number, limit, power):
    answer = 0 
    for i in range(1,number+1):
        if count_divisors(i) > limit:
            answer+=power
        else:
            answer+=count_divisors(i)
        
    return answer