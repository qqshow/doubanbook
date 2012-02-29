import re,urllib,cookielib,urllib2
import socket
socket.setdefaulttimeout(5)
def sortDic(Dict):
        return sorted(Dict.items(),key=lambda e:e[1])

class crawl:
	def __init__(self,ini):
		self.pages=[]
		self.pages.append(ini)
		self.add=True
		
	def PageParser(self,page):
		print page
		directions=re.findall(r'\s*href\s*=\s*"(https?://[^"^\s^\(^\)]*)',page)
#only add new pages when less then 100 pages		
		if len(self.pages)>10:
			self.add=False
		if self.add==True:	
			for direccion in directions:
				if not direccion.endswith(".js") and not direccion.endswith(".css") and not direccion.endswith(".exe") \
				and not direccion.endswith(".pdf"):
					self.pages.append(direccion)
				print self.pages
	
	def PageLoad(self,dir):
		print dir
		page=urllib.urlopen(dir)
		self.PageParser(page.read())
	
	def crawl_pages(self):
		while len(self.pages)!=0:
			self.PageLoad(self.pages.pop(0))

class douban(object):
    def __init__(self):  
        self.app = ''  
        self.signed_in = False  
        self.cj = cookielib.LWPCookieJar()  
        try:  
           self.cj.revert('douban.coockie')  
        except:  
            None  
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
        urllib2.install_opener(self.opener)  
    def setinfo(self,username,password,domain,origURL):
                self.name=username
                self.pwd=password
                self.domain=domain
                self.origURL=origURL
    def signin(self):  
        i=0
        params = {'form_email':self.name, 'form_password':self.pwd, 'remember':1}  
        req = urllib2.Request(  
            'http://www.douban.com/login',  
            urllib.urlencode(params)  
        )  
		
        r = self.opener.open(req)
        if r.geturl() == 'http://www.douban.com/':  
            print 'Logged on successfully!'  
            self.cj.save('douban.coockie')  
            self.signed_in = True
            page=urllib.urlopen("http://www.douban.com")
            print page.read()
            return 0
        return 1
 
