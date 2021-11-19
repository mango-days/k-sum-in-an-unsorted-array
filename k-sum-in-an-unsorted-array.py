import math

array = [ 10, 12, 9, 8, 10, 15, 1, 3, 2 ]
n = len( array )
k = 3
max_sum = -math.inf
    
for index in range ( 0 , n-k+1 ) :
    temp_sum = 0
    for i in range ( index , index+k-1 ) :
        temp_sum += array [ i ]
        if ( i+2 == index+k ) : temp_sum += array [ i+1 ]
    if temp_sum > max_sum : max_sum = temp_sum
print ( max_sum )
