 def trapezoid(f,a,b,n):
		h = float(b-a)/n
    hasil = 0.5*f(a) + 0.5*f(b)
		for i in range(1,n):
			hasil += f(a+i*h)
		hasil *= h
    return hasil
