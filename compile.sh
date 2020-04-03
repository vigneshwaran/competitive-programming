if [ ! -z "$i"] ; then
g++ $1
fi;
s=`pwd`'/testcases/'
for i in `ls testcases/inp`; 
do 
./a.out < $s'inp/'$i > pred;
line=`diff pred $s'op/'$i`;
if [ -z "$line" ] ; then
        echo "Success"
else
    echo "Fails"
    echo $line
fi;
done