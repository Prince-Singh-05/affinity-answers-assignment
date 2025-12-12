#!/bin/bash

curl -s "https://www.amfiindia.com/spages/NAVAll.txt" |
awk -F ';' '
{
    scheme=$4;
    nav=$5;
    if (scheme != "" && nav != "")
        print scheme "\t" nav;
}' > nav_output.tsv
