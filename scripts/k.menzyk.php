<?php $o=$argv[1];$w=$o*2;for($r=0;$r<$o+$argv[3];$r++){for($c=0;$c<$w*$argv[2];$c++){$z=$r*2;$y=$c%$w-($w-$z)/2;echo$r<$o?($y<-1||$y>=$z?' ':($y<0||$y+1==$z?"\033[93m*":(($y+2*($r%2))%4<1?"\033[97m$":"\033[32m#"))):($y==$z/2-1?"\033[91mH":' ');}echo"\n";}echo str_repeat("\033[97m^",$w*$argv[2]-1)."\n";