sigma=0
n=6
for i in range (3, n+1):
    sigma= sigma + i*i
    print(sigma)

#notasi Phi
phi=1
a=21
for i in range(2, 5*a-6):
    phi= phi*i
    print(phi)

#code Number python
import numpy as np
b=np.matrix ([[4,-2,7],[1,5,3]])
print("b=\n",b)
print (type(b))

#code array 
A= np.array ([[4,-2,7],[1,5,3]])
print("A = /n",A)
print(type(A))
#matriks nol
o= np.zeros([5,5])
print(o)
#matriks satu berukuran 5x5
j= np.ones([5,5])
print(j)
#matriks identitas berukuran 5x5
i=np.eye(5)
print(i)
#oprasi matriks
x= np.array([[ 1,0,0,4 ],[]])
y= np.array([[3,5],[2,-2]])
z= np.array([[4,2],[2,2]])
#menjumlahkan 2 matriks
print(y+z)
#mengalikan matriks dengan skalar
print(10*x)
#mengalikan matriks dengan matriks
print(y@z)
#menggunakan matmul syaratnya kolom di y harus sama dengan baris di z
r= np.matmul(y,z)
print(r)
#sama kaya matmul
s= np.dot(y,z)
print(s)
#transpose matriks
t= A.transpose()
print(t)
#determinan matriks
det=np.linalg.det(y)
print(det)
#invers matriks
inv=np.linalg.inv(z)
print(inv)
