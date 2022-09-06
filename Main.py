import sys
sys.dont_write_bytecode = True
import os
import api

print("WARNING YOU NEED TO MAKE A FOLDER CALLED YIFF AND RUN THIS IN THERE YOU HAVE 10 SECONDS TO CONTINUE OR CLOSE THIS CONSOLE")
print(10)
api.pause()
print(9)
api.pause()
print(8)
api.pause()
print(7)
api.pause()
print(6)
api.pause()
print(5)
api.pause()
print(4)
api.pause()
print(3)
api.pause()
print(2)
api.pause()
print(1)
api.pause()

print("Enjoy Moving those paws!~ ;3")


os.mkdir("Gay")
os.mkdir("Lesbian")
os.mkdir("Striaght")
os.mkdir("Trans")

for path_items in map(api.concat, api.Artists):
    api.make(path_items)

api.end()