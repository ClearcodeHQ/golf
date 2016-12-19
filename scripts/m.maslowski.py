import sys;w,N,R=map(int,sys.argv[1:]);W='[';m,Y,Z,D=W+'32m#',W+'93m*',W+'91mH',W+'97m$';D,W,S=(m+m+D+m)*w,W+'97m^',' ';A=S*(w-1)
for l in[A+Y+A+S]+[S*(w-p-2)+Y+D[12*p:24*p+6]+Y+S*(w-p-1)for p in range(w-1)]+[A+Z+A+S]*R:print l*N
print(2*w*W*N)[:-6]
