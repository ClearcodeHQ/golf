import sys
l=int
d=range
i=sys.argv
r=l(i[1])
w=l(i[2])
T='\033[%dm'
b=''
x=lambda x:x.center(r*2)*w+'\n'
for n in d(r):j=2*n;b+=x(('*'+('###$'*9+'##*')[-j:],'*')[j==0])
b+=x('H')*l(i[3])+'^'*(r*2*w-1)
d={'*':T%93,'$':T%97,'#':T%32,'H':T%91,'^':T%97}
for c in d:b=b.replace(c,d[c]+c)
print b