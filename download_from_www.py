import os as os
import urllib.request
import urllib.request as url

# path to actuall folder of project
#data_dir = os.path.dirname(__file__)
data_dir='C:/Users/pj3dmv/Desktop/WWW STRONY'
print(data_dir)

pages = [

    { 'name': 'mobilo','url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy','url': 'http://www.kursyonline24.eu/'} ]

path =[]
for i in range(0,len(pages)):
    path.append(data_dir + pages[i]['url'] + ".html")
    urllib.request.urlretrieve("http://www.google.pl",data_dir)




