- `BASH_SOURCE[0]` retuns the path of the script regardless where it is called from
- `-q` in grep stands for quite opposite to verbose
- `||` means run the RHS command if LHS fails and similarly && means dont run RHS command if LHS fails
- `-s` in 'test' stands for check if file is not empty 
- `-r` in read means, treat `\` as literals
- read command can read more than one input from stdin
- `&>` stands for redirection of `stdin + stderr`
- `2>&1` means `stderr` goes where `stdin` goes
- `!` infront of variable stands for indirect access of a variable. basically it treats the contents of variable as another variable.

## Associative arrays
```
declare -A <name>   # to declare
```

```
<name>["<key>"]="<value>"   # to insert key and values
```

```
echo "${!<name>[@]}"   # all keys
echo "${<name>[@]}"    # all values
```

```
[[ -v <name>["<key>"] ]]    # This checks existence, not value.
```



