import os
import re

from myexperiance import fileoperation as file_module



print(file_module.readmode)
print(file_module.readtofile('labtext.txt'))

print("-------------------------")

print(os.getcwd())
print("---------------")
print(os.system('dir'))
print("---------------")
print(os.listdir('/'))

print("-------------------------")

str = "welcom, in my page"
pattern = re.search("^Hello.rania.",str)
print(pattern)

print("-------------------------")



import pys

conn = pys.connect(database='RaniaDB',host='localhost',user='rania',password='1234')
cur = conn.cursor()
cur.execute("SELECT * FROM result;")
rows = cur.fetchall()
conn.close()