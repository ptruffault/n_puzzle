#!/bin/zsh
rm -rf "$(dirname -- "$0")/taquin_*.txt"
for ((i=3;i<=10;i++));do 
   CMP="$(python3 "$(dirname -- "$0")/../../../src/npuzzle.py" "$(dirname -- "$0")/taquin_$i.txt")" 
   if [[ "$CMP" = *invalid* ]]; then
    	echo "$(dirname -- "$0")/taquin_$i.txt : \033[1;32mOK\033[0m"
	else
    	echo "\033[0;31m$(dirname -- "$0")/taquin_$i.txt : KO'\033[0m"
    	echo $CMP
	fi
done