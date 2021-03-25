echo "TEST SOLVABLE"
zsh "$(dirname -- "$0")/maps/solvable/test.sh"
echo ""

echo "TEST UNSOLVABLE"
zsh "$(dirname -- "$0")/maps/unsolvable/test.sh"
echo ""

echo "TEST SOLVED"
zsh "$(dirname -- "$0")/maps/solved/test.sh"
echo ""

