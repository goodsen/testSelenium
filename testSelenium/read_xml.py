from xml.dom import minidom

#parse打开xml文档
dom = minidom.parse(r'info.xml')
#documentElemen得到文档元素对象
root = dom.documentElement
logins = root.getElementsByTagName('login')
#获得login标签的username属性值
username = logins[0].getAttribute("username")
print(username)
#获得login标签的password属性值
password = logins[0].getAttribute("password")
print(password)
#获得第二个login标签的username属性值
username = logins[1].getAttribute("username")
print(username)
password = logins[1].getAttribute("password")
print(password)
#tagname = root.getElementsByTagName('bowser')


#print(root.nodeName)
#print(root.nodeValue)
#print(root.nodeType)
#print(root.ELEMENT_NODE)