# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class HtmlParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
        
    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))


html = ""

for i in range(int(input())):
    html += input()


html_par = HtmlParser()

html_par.feed(html)
