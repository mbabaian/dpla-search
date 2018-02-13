# Practicing call to DPLA and getting data from it, then displaying results via html
import sys # this is needed for command line arg
import webbrowser
from operator import itemgetter
import requests

f=open('result.html', 'w')

keyword = sys.argv[1]
#size = sys.argv[2]

# Make an api call and store the response.
url = "https://api.dp.la/v2/items?q=" + keyword + "&api_key=aefc7b2874411888e4e06b515935c19c" #only returns 10

#url = "https://api.dp.la/v2/items?q=" + keyword + "&page_size=" + size + "&api_key=aefc7b2874411888e4e06b515935c19c"

r = requests.get(url)
print('Status code: ', r.status_code)

# Process information from each item
data = r.json()
data_list = []

# Everything before the list goes in header
header = """<html>
    <head>
        <title> Practice </title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"></link>
        <style>
            #body { background-color: #dd6021; color: white; }
            a { color: ##53bcbb;}
            h1 { padding-left: 100px; color:#53bcbb; }
            p { color: #4b4b4f; margin: 20px 0 20px 100px; font-size: 1.25em; }
            h3 { color: #4b4b4f; margin: 20px 0 0 100px;}
            h4 {text-align:center; padding: 30px 0 20px 0;}
            h5 { padding-left: 100px; color: #4b4b4f; margin: 30px 0 0 0; }
        </style>        
    </head>        
    <body>
        <div class="jumbotron jumbotron-fluid">
        <h1> Practicing Python Queries to HTML Data </h1>
        <h3> This is a Python program that searches DPLA and creates static website of the results.</h3>
        <h5> Default search results limited to 10. Number of results can be increased if third command line argument is used.</h5>
        
        </div>"""

# put the list in the docs variable
docs = ""
for d in data['docs']: 
    # print('Title:',  d['sourceResource']['title'])
    # print('Source:', d['dataProvider'])
    # print('URL:', d['isShownAt'])

    title = d['sourceResource']['title']
    source =d['dataProvider']
    link = d['isShownAt']
    
    message = """<p><strong>Title: </strong><a href="%s"> %s</a><br><strong>Location: </strong>%s</p>"""
    # pass results from python query to html display
    result = message  % (link, title, source)
    docs += result

# put everyting after the list in footer
footer = """</body>
        <h4>Created by Monica Babaian</h4>
    </html>"""
           

# write all data to html file
f.write(header)
f.write(docs)
f.write(footer)
f.close()

webbrowser.open_new_tab('result.html')