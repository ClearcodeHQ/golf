#!/bin/bash
e(){ echo -en "$1"; }
G='\033[32m'
R='\033[91m'
W='\033[97m'
Y='\033[93m'
NS=$1
NT=$2
NTR=$3
ph(){
NP=$(($2 + $NS%2));
for i in `seq 1 $1`;{
((($NP%2==0&&($i+3)%4==0)||($NP%2==1&&($i==3||(($i+1)%4==0)))))&& e "${W}\$"||e "${G}#"
}
}
d(){
for i in `seq 1 $1`;{
e "$2"
}
}
pss(){
e $Y*
}
pt(){
e ${R}H
}
for l in `seq 0 $((NS-1))`;{
for t in `seq 0 $((NT-1))`;{
d $((NS-l-1)) ' '
pss
if (($l!=0)); then
ph $((l*2-1)) $((NS-l))
pss
fi
d $((NS-l)) ' '
}
echo
}
for l in `seq 0 $((NTR-1))`;{
for t in `seq 0 $((NT-1))`;{
d $((NS-1)) " "
pt
d $NS " "
}
echo
}
d $((NS*NT*2-1)) "$W^"
echo
