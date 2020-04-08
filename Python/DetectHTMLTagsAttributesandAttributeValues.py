# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class HtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
    

html_parser = HtmlParser()
html_text = ""

for i in range(int(input())):
    html_text += input()
    html_text += '\n'

html_parser.feed(html_text)

