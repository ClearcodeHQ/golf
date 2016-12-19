import sys
x,y,z=map(int,sys.argv[1:])
a='\033['
b=' '
s=a+'93m*'
h=a+'32m#'
for i in range(x):
	o=b*(x-i-1)
	print(o+s+((h*3+a+'97m$')*x+h*2+s+b)[-i*12-1:]+o)*y
while z:
	print(b*(x-1)+a+'91mH'+b*x)*y
	z-=1
print(a+'97m^')*(2*x*y-1)