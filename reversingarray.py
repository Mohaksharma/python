import array as arr
# sindex and lindex: denotes the starting and last index of the array.
def reverse(sindex, lindex, myarray):
    while(sindex < lindex):
        myarray[sindex], myarray[lindex-1] = myarray[lindex-1], myarray[sindex]
        sindex += 1
        lindex -= 1
        
if __name__ == '__main__':
    myarray = arr.array('i',[1,2,3,4,5,6])
   # myarray.insert(2, 2)
   # myarray.insert(1, 3)
   # myarray.insert(3, 1)
    print('Array before Reversing:',myarray)
    reverse(0, len(myarray), myarray)
    print('Array after Reversing:',myarray)
