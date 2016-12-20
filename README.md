# Clearcode Golf

![tree](/tree.png)

## Description

The purpose of this challenge is to write a shortest code to render ASCII christmas trees (forest?). You may find examples in the `tree.png` and in `check` directory 

### Technicals

Chars: `*#$H^` and space

Colors: (http://misc.flogisoft.com/bash/tip_colors_and_formatting)

```
GREEN = '\033[32m'
RED = '\033[91m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
```

### Rules

1. Every line ends with `\n`
2. The solution should consist of only 1 file 
3. Other scripts (online/from disk) and libs are not allowed (except stdlib)
4. Every char (expect space) starts with the color code (see technicals above)
5. Arguments are always positive integers

## Test

```
cd check/
./check.sh interpreter patch_to_file_with_code
```

### Example

```
./check.sh python ~/tree/xxx_tree.py
MERRY CHRISTMAS size: 233 /home/xxx/tree/xxx_tree.py \r count: 0
```

## HIGHSCORE

### PYTHON

1. 220b Daniel O.
2. 233b Pyszo
3. 251b Michał M.
4. 264b Marcin M.
5. 291b Patryk P.

### PHP

1. 305b Krzysiu M.
2. 334b Zeulus
3. 345b Marcin Wi.

### JS

1. 255b Pyszo
2. 285b Krzysiu M.
3. 339b Witek G.

### BASH

1. 594b Urug

