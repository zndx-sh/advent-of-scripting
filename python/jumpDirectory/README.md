i recently learned some basic of argparse from this [tutorial](https://docs.python.org/3/howto/argparse.html)\
it was a good experience.

so there are something called positional arguments and optional arguments  
positional args, according to my understanding having names with no leading dashes  `-` but for optional args, there are leaded by two dashes  `--` 

- `os.path.realpath` resolves symlinks and relative paths to absolute paths
- `os.path.dirname` is similar to bash `dirname`, where it gets the directory path of the currently running file
- `nargs` tells how many arguments should be consumed by a flag. Default value is 1. `?` means consume 0 or 1 value
- `os.environ` can access environment variables
- `writelines` takes multiple lines as input (iterator) in contrast to `write`, which only takes one line. Both preserve newline characters

apparently i just found out that a script cannot change my CWD as it runs as a child process of my terminal process.
```
zsh ---> parent process
  |
  |- jumpdir.py --> child process
  |- someOtherProcess.py
```