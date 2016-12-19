import sys
T='[32m#'
S='[93m*'
h,a,m=map(int,sys.argv[1:])
def P(v,i=h-1,c=' '):print(c*i+v+c*i+c)*a
P(S)
for i in range(1,h):P(S+((T+'[97m$'+T+T)*h)[6-i*12:]+S,h-i-1)
while m:P('[91mH');m-=1
print'[97m^'*(a*h*2-1)
