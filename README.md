# Caesar/Shift Cypher

## PR for this file: 

This is Lab 17 of 401-Python (seattle-py-401n2)

Developers: Kim Damalas

Date: 3 February 2021
____________________
### Features

1. Scrape a Wikipedia page and record which passages need citations.
    - E.g. History of Mexico has 7 “citation needed” cases, as of this writing.

2. Your web scraper should report the number of citations needed

3. Your web scraper should identify those cases AND include the relevant passage.

    - E.g. Citation needed for “lorem spam and impsum eggs

    - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

4. Count function must be named `get_citations_needed_count`
    - `get_citations_needed` takes in a url and returns an integer

5. Report function must be named `get_citations_needed_report`
    - `get_citations_needed_report` takes in a url and returns a string

    - the string should be formatted with each citation needed on own line, in order found.

6. Module must be named scraper.py
__________

## Approach

Approach is using data `requests` to the website and `beautifulsoup4 or bs4` to parse and filter data received from the site. User will need to add dependencies listed in import list (or .toml file) of scraper.py before running scraper.py

_____________
## Required User Acceptance Testing

1. verify that correct count of citations needed is calculated

2. verify that preceding passage


_________________


