#!/bin/zsh
rm -rf "$(dirname -- "$0")taquin_*.txt"
for ((i=3;i<=8;i++));do 
   python3 "$(dirname -- "$0")/../../npuzzle-gen.py" -s $i |sed -e '/^[ \t]*#/d'|tr '\n' '-'|tr -d ' '|sed "s/--/+/g"|tr '+' '\n'|tr '-' ' '|sed '0,/ /s//\n/' > "$(dirname -- "$0")/taquin_$i.txt"
   python3 "$(dirname -- "$0")/../../../src/npuzzle.py" "$(dirname -- "$0")/taquin_$i.txt" 
done