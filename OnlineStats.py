# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes
PROGRAMMING ASSIGNMENT #1
'''
# =============================================================================
print("\n")
print("CPSC-51100, Summer II 2019", "NAME: Amy Noyes", \
      "PROGRAMMING ASSIGNMENT #1", sep="\n")
      
print("\n")
 
print("Welford's Online Algorithm", \
      "Mean = x ̅n = x ̅n-1 + (xn - ̅x n-1)/n", \
      "Sum of squares of differences from the current mean = M2,n = (M2,n-1) + (xn -  x ̅n-1)(xn - x ̅n)", \
      "Sample Variance= S2n = (M2,n)/(n-1)", sep="\n")


count = 0
variance = 0
mean = 0
M2 = 0

#Program ends if user enters non-negative number
while True:
    num = float(input("Enter a number: "))
    if num < 0:
        break
    count += 1

#if number entered is 1
    if count == 1:
        mean = num
        variance = 0

#for numbers greater then 1        
    else:
        delta = num - mean
        mean += delta / count
        delta2 = num - mean
        M2 += delta * delta2
        variance = (M2/(count - 1))
        
    print('Mean is {} variance is {}'.format(mean, variance))

