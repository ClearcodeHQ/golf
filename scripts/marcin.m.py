import sys
h,n,q=map(int,sys.argv[1:])
p,l='\033[9',h-1
z='\033[32m#'
t=p+'7m$'+2*z
for i in range(h):print(' '*(l-i)+p+'3m*'+(('',z)[i>0],('',z*2)[i%2]+(i/2-1)*(t+z)+t)[i>1]+('',p+'3m*')[i>0]+' '*(h-i))*n
print((' '*l+p+'1mH'+' '*h)*n+'\n')*q+(p+'7m^')*(2*h*n-1)
