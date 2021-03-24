#!/bin/zsh
rm -rf "$(dirname -- "$0")/maps/solvable" "$(dirname -- "$0")/maps/unsolvable"
mkdir "$(dirname -- "$0")/maps/solvable" "$(dirname -- "$0")/maps/unsolvable"
for ((i=3;i<=9;i++));do
   python3 "$(dirname -- "$0")/npuzzle-gen.py" -s $i |sed -e '/^[ \t]*#/d'|tr '\n' '-'|tr -d ' '|sed "s/--/+/g"|tr '+' '\n'|tr '-' ' '|sed '0,/ /s//\n/' > "$(dirname -- "$0")/maps/solvable/taquin_$i.txt"
   python3 "$(dirname -- "$0")/npuzzle-gen.py" -u $i |sed -e '/^[ \t]*#/d'|tr '\n' '-'|tr -d ' '|sed "s/--/+/g"|tr '+' '\n'|tr '-' ' '|sed '0,/ /s//\n/' > "$(dirname -- "$0")/maps/unsolvable/taquin_$i.txt"
done