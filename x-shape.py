"""
print this pattern using only # and \n

#            #
 ##        ##
  ###    ###
   ########
   ########
  ###    ###
 ##        ##
#            #

Analysis:
14 width
8 height

row    side        center-gap            hashes
--------------------------------------------------------
4       4-row   (7-(side+hashes))*2      side+1
3       4-row
2       4-row
1       4-row
0 skip
1       4-row
2       4-row
3       4-row
4       4-row

"""

for i in range(4, -5, -1):
    if i == 0:
        continue
    positive = abs(i)
    side = 4 - positive
    hashes = side + 1
    center = (7 - (side + hashes)) * 2
    print(f"{side * ' '}{hashes * '#'}{center * ' '}{hashes * '#'}{side * ' '}")
