# amazonJp
This project is to crawl data from amazon(Japan).

# Usage Scenario
 1. Open Japanese amanzon website, input a keyword, then click 'Search' button;
 2. Get a list of items that matching the keyword, then get offer shops' links of each item.

# Requirements
 1. Python2.7+ (not version 3)
 2. Python Lib: bs4, lxml

# How to use
 Open the searchlist.txt file, type in the searching words(each word a single line);
 Open a terminal, use command 'python crawler.py';
 Finally, the parsing result will be in the data directoy, the file is named with each searching word.

# Update
 1. Add stategy to crawl bestseller(first three) of each category in amazon.co.jp;
 2. Add method to convert asin of amazon to common used eancode(jp);
