from util import *
import re,urllib,urllib2


dou=douban()
username='bhlx88@gmail.com'
password='xxxxxx'
domain='http://www.douban.com/'
origURL='http://www.douban.com/login'
dou.setinfo(username,password,domain,origURL)
dou.signin()
page=dou.opener.open('http://www.douban.com/contacts/list')
directions=re.findall(r'\s*href\s*=\s*"http://www.douban.com/people/([^/]*)',page.read())
dir={}
dir_book={}
book_names = {}
i=0
for direction in directions:
    dir[direction]=0
num=len(dir)
i=0
for nam, nothing in dir.items():
    name="http://book.douban.com/list/"+nam+"/collect"
    print name
    #i=i+1
    print "books of",nam,":"
    page=dou.opener.open(name)
    while True:
        p=page.read()
        books=re.findall(r'href="(http://book.douban.com/subject/.*/)"\sclass',p)
        booknames=re.findall(r'<em>([^<]*)</em>\s+</a>',p)

        for book in books:
            print book
            if book in dir_book:
                dir_book[book]=dir_book[book]+1
            else:
                dir_book[book]=1
        for bookname in booknames:
            print bookname.decode('utf-8').encode('mbcs')     
        ds=re.search(r'<link rel="next" href="(http://[^"]*)"/>',p)      
        if ds == None:
            break
        page=dou.opener.open(ds.group(1))     
        
for book_name,times in sortDic(dir_book):
    print book_name+": "+str(times)
print len(dir_book) 
    
