import ctypes as C

math = C.CDLL('./libmymath.so')

math.add_int.restype 	 = C.c_int
math.add_int.argtypes 	 = [C.c_int,C.c_int]
math.add_float.restype 	 = C.c_float
math.add_float.argtypes  = [C.c_float,C.c_float]
math.dot_product.restype = C.c_float

n 		= C.c_int(218)
m 		= C.c_int(-14)
res0 	= C.c_int()
math.add_int_ref(C.byref(n),C.byref(m),C.byref(res0))

f 		= C.c_float(18.7)
g 		= C.c_float(-4.7)
res1 	= C.c_float()
math.add_float_ref(C.byref(f), C.byref(g), C.byref(res1))

k 		= C.c_int(4)
v 		= (C.c_int * 4) (8,-4,0,17) 
w 		= (C.c_int * 4) (-8,24,1,1)
res2 	= (C.c_int * 4) ()
math.add_int_array(C.byref(v), C.byref(w), C.byref(res2), k)

u 		= (C.c_float * 4) (8.0,-4.0,0.0,17.0) 
z 		= (C.c_float * 4) (-8.0,24.0,1.0,1.0)
res3	= math.dot_product(C.byref(u), C.byref(z), k)

u 		= (C.c_float * 4) ( 8.0,4.0,0.0,15.0) 
z 		= (C.c_float * 4) (-8.0,2.0,1.0,1.0)
res4	= math.dot_product(C.byref(u), C.byref(z), k)

print math.add_int(18,-2)
print math.add_float(18.7,-2.7)
print res0.value
print res1.value

print res2[0],res2[1],res2[2],res2[3]
print res3, res4