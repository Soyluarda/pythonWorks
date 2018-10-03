import requests
import dryscrape

r = requests.get("http://avi.im/stuff/js-or-no-js.html")
r.content ## javascript'in etki ettigi alanlari gostermez.

s = dryscrape.Session()
s.visit("http://avi.im/stuff/js-or-no-js.html")
s.body() ## now we can see javascript results.
