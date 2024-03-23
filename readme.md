## Coding Challenges - Challenge 1
[link](https://codingchallenges.fyi/challenges/challenge-wc)

### cli option "-c" -> outputs the "number of bytes" in a file.
```
>ccwc -c ./sample-text/test.txt
  342190 ./sample-text/test.txt
```

### cli option "-l" -> outputs the "number of lines" in a file.
```
>ccwc -l ./sample-text/test.txt
    7145 ./sample-text/test.txt
```

### cli option "-w" -> outputs the "number of words" in a file.
```
>ccwc -w ./sample-text/test.txt
   58164 ./sample-text/test.txt
```

### cli option "-m" -> outputs the "number of characters" in a file.
<!-- If the current locale does not support multibyte characters this will match the -c option. -->
<!-- Refer to this link -> [locale reference](https://learn.microsoft.com/en-us/globalization/locale/locale) -->
```
>wc -m ./sample-text/test.txt
  339292 ./sample-text/test.txt

>ccwc -m ./sample-text/test.txt
  339292 ./sample-text/test.txt
```

### default option -> (i.e. no options are provided) which is the equivalent to the -c, -l and -w options.
```
>ccwc ./sample-text/test.txt
    7145   58164  342190 ./sample-text/test.txt
```

### support being able to read from standard input if no filename is specified.
```
>cat ./sample-text/test.txt | ccwc -l
    7145
```

# Setup
1. Create a virtual environment:<br/ >
  `python -m venv venv`

2. Add the `ccwc` cmd to the virtual envoronment: <br />
  `pip install -e <path>` 
  <br />(-e stands for editable: It directly reflects the changes in the module implementation!)
  <br />(path -> path of the setup.py file)
