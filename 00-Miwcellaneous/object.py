import sys

n = 10
print("n = 10\nn id : ", id(n), "\tRefCount : ",sys.getrefcount(n))
m = n
print("m = n\nm id : ", id(m), "\tRefCount : ",sys.getrefcount(m))
k = 20
print("k = 20\nk id : ", id(k), "\tRefCount : ",sys.getrefcount(k))
o = n
print("o = n\nm id : ", id(o), "\tRefCount : ",sys.getrefcount(o))
print('\n\n')

l = 121212121143543534098734905739457394750395
print('l = ',l,'\nl id : ', id(l),'\tRefCount : ',sys.getrefcount(l))
p = l
print('p = l','\np id : ', id(p),'\tRefCount : ',sys.getrefcount(p))

q = 121212121143543534098734905739457394750395
print('q = ',q,'\nq id : ', id(q),'\tRefCount : ',sys.getrefcount(q))
