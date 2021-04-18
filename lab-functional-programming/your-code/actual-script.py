# Import libraries
import pandas as pd
import re

# Load html file
html_list = []
for line in open('./www.lipsum.com.html'):
    html_list.append(line)
# print(html_text)

def valid_corpus(html_list):
    valid_tags = ['h1','h2','h3','h4','h5','h6','p','strong']
    valid_text = []
    v_text=''
    for row in html_list:
        for v_tag in valid_tags:
            start = "<"  + v_tag +">"
            end   = "</" + v_tag +">"
            # start = '<h3>'
            # end = '</h3>'
            if start in row:
                # valid_text += (row.split(start))[1].split(end)[0]
                v_text = re.search('%s(.*)%s' %(start,end), row).group(1)
                valid_text.append(v_text)
    return valid_text

print(valid_corpus(html_list))
