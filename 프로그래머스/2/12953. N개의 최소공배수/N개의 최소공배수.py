import math
def solution(arr):
    for k in range(len(arr)-1):
            gcd=math.gcd(arr[k],arr[k+1])
            lcm=arr[k]*arr[k+1]//gcd
            arr[k+1]=lcm
    return lcm