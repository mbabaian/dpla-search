# dpla-search

## About
Python program that takes in a search term from the command line, searches Digital Public Library of America's databases, and returns an HTML document showing the first ten results from the search. 

## How it works
From the command line:
```
python dpla_search.py penguins
```
The program will automatically create a website showing the results of the search:

![image](https://github.com/mbabaian/dpla-search/blob/master/dpla_search.png)

#### Changing Number of Items Returned
By default, DPLA returns the first ten items in any search query. You can change the code in this program to return more or fewer than ten results by adding a second command line argument (see line 10 in ```dpla_search.py```). Then comment out line 13 and make line 15 active. Run the program from the command line:
```
python dpla_search.py penguins 30
```

## Rationale
I created this program out of personal curiosity for exploring how Python can be used as a backend for web development. 

## Technologies
#### Front end 
HTML/CSS/Bootstrap
#### Back end 
Python 3.0

### License
[MIT](https://opensource.org/licenses/MIT)
