array = [ 10, 12, 9, 8, 10, 15, 1, 3, 2 ]
n = len( array )
k = 3

# initial value of window
temp_sum = sum( array [ :k ] )
max_sum = temp_sum

# window is now sliding
for index in range ( k , n ) :
    temp_sum
    temp_sum = temp_sum - array [ index-k ] + array [ index ]
    if temp_sum > max_sum : max_sum = temp_sum
    
print ( max_sum )
