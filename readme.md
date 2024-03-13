# cli option -c -> outputs the "number of bytes" in a file.
```
>ccwc -c test.txt
  342190 test.txt
```

# cli option -l -> outputs the "number of lines" in a file.
```
>ccwc -l test.txt
    7145 test.txt
```

# cli option -w -> outputs the "number of words" in a file.
```
>ccwc -w test.txt
   58164 test.txt
```

# cli option -m -> outputs the "number of characters" in a file.
<!-- If the current locale does not support multibyte characters this will match the -c option. -->
<!-- Refer to this link -> [locale reference](https://learn.microsoft.com/en-us/globalization/locale/locale) -->
```
>wc -m test.txt
  339292 test.txt

>ccwc -m test.txt
  339292 test.txt
```

# default option -> (i.e. no options are provided) which is the equivalent to the -c, -l and -w options.
```
>ccwc test.txt
    7145   58164  342190 test.txt
```

# support being able to read from standard input if no filename is specified.
```
>cat test.txt | ccwc -l
    7145
```