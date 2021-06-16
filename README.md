## Checking the links on the digital-land site

The validity of links on the site can be checked using the [w3c link checker](https://metacpan.org/dist/W3C-LinkChecker).

# Usage

`-D` specifies recursion depth

`-X` specifies an exclusion (regex)

This will take some time to run. Using `tee` allows the output to be viewed in real-time as well as written to the output file.

```
/usr/local/Cellar/perl/5.32.1_1/bin/checklink -sber -t10 -D5 -qi -X '(digital-land\\.github\\.io\\/organisation\\/|digital-land\\.github\\.io\\/conservation-area\\/|digital-land\\.github\\.io\\/brownfield-land\\/|digital-land\\.github\\.io\\/collection\\/|digital-land\\.github\\.io\\/parish\\/|digital-land\\.github\\.io\\/weeknote\\/|digital-land\\.github\\.io\\/site\\.webmanifest)'  digital-land.github.io | tee checklink.out
```

# Post-processing

The output of `checklink` can be post processed into a csv file to make for easier filtering and tracking.

```
cat checklink.out | python link-check-formatter.py > checklink.csv
```
