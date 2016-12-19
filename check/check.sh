#!/bin/bash
for a in {3..15..3}; do
    for b in {1..5}; do
        for c in {1..5}; do
            $1 $2 $a $b $c 2> /dev/null | diff $a-$b-$c -
            if [[ $? -ne 0 ]]; then
                echo problem with args: $a $b $c
                exit
            fi
        done
    done
done
echo MERRY CHRISTMAS size: $(wc -c $2) \\r count: $(grep -c $'\r$' $2)
