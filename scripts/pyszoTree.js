let[,,x,y,z]=process.argv,f=(m,n)=>m.repeat(n),a='\033[',b=' ',s=a+'93m*',h=a+'32m#',i=0,r=console.log;while(i<x)r(f(f(b,x-1-i)+s+(f(h+h+h+a+'97m$',x)+h+h+s+b).slice(-i++*12-1)+f(b,x-i),y));while(z--)r(f(f(b,x-1)+a+'91mH'+f(b,x),y));r(f(a+'97m^',2*x*y-1))