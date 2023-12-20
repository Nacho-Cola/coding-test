def solution(number, limit, power):
    sums = []
    for i in range(1,number+1):
        sumgcd = 0
        for j in range(1,int(i**.5)+1):
            if i%j == 0: 
                if i//j == j:
                    sumgcd +=1
                else:
                    sumgcd +=2
        sums.append(sumgcd)
    sums = map(lambda x: power if x > limit else x, sums)
    return sum(sums)
