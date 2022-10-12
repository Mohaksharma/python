import array as arr
def rotate(rotateby, a):
    for i in range(0,rotateby):
        rotateone(a)
    return a
def rotateone(a):
    for i in range(len(a)-1):
        a[i],a[i+1] = a[i+1],a[i]

if __name__ == '__main__':
    a = arr.array('i',[11,2,5,6,3,21,33])
    print('before rotation : ',a)
    print('after rotation : ',rotate(1,a))
