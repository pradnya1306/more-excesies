
def max(marks):
    for j in range(len(marks)):
        max=0
        for i in range (len(marks[j])):
            if marks[j][i]>max:
                max=marks[j][i]
        print(max)

marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
max(marks)




# big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
# for i in range(len(big_list)):
#     for j in range( len(big_list[i])):
#         print (big_list[i][j])
#     print ('-----')
