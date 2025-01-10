if statements in Bash are often used in four important ways:

1. if...then...fi statements
2. if...then...fi...else statements  
3. if..elif..else..fi  
4. if..then..else..if..then..fi..fi.. (Nested Conditionals)
Their structure is

if [[ condition ]]
then
	do this
elif [[ condition ]]; then
	do this
else
	do this by default
fi

Note that there must be spaces between the brackets and their enclosing text. An or condition is || and an and condition is &&.
Also note that then is required after if and elif but not after else. It must be separated from the conditional by either a newline or a ; which represents a newline to bash.
The entire if clause is terminated with fi.
