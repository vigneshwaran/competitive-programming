# takes .cpp and problem index
g++ $1 -o temp.out
out=temp.out

s='testcases/'$2

for i in `ls $s/inp`
    do 
        ./$out < $s'/inp/'$i > pred
        line=`diff pred $s'/op/'$i`
        
        if [ -z "$line" ] 
        then
            echo "Success"
        else
            echo "Fails"
            echo $line
        fi
    done