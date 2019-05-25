
e.g. for string "abba". we will create the following lookup table.


| index |       |   0   |   1   |   2   |   3   |
| :---: | :---: | :---: | :---: | :---: | :---: |
|       | char  |   a   |   b   |   b   |   a   |
|   0   |   a   |   T   |       |       |       |
|   1   |   b   |       |   T   |       |       |
|   2   |   b   |       |       |   T   |       |
|   3   |   a   |       |       |       |   T   |

$\Downarrow$

| index |       |   0   |   1   |   2   |   3   |
| :---: | :---: | :---: | :---: | :---: | :---: |
|       | char  |   a   |   b   |   b   |   a   |
|   0   |   a   |   T   |   F   |   F   |   T   |
|   1   |   b   |       |   T   |   T   |   F   |
|   2   |   b   |       |       |   T   |   F   |
|   3   |   a   |       |       |       |   T   |



lookup[1:2] is true which means the given string s[1:2] is palindrome.

minCut[i] list indicate how many cuts needed from i to end

|   0   |   1   |   2   |   3   | 4   |
| :---: | :---: | :---: | :---: | --- |
|   a   |   b   |   b   |   a   |     |
|   0   |   2   |   1   |   0   | -1  |
