import urllib2
import re

req = urllib2.Request('http://python.org')

response = urllib2.urlopen(req)
the_page = response.read()
print the_page

print "------------------------------------------------------------------"
print len(the_page)
print "------------------------------------------------------------------"
links = re.findall('"((http|ftp)s?://.*?)"', the_page)
for link in links:
    print link
print "------------------------------------------------------------------"
