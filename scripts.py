from sys import argv
import subprocess

script, filename = argv

print "Creating file " + filename

file = open(filename, 'w')
file.write("Thi file was made with python")
file.close()

print("Finished")



name = str(script)

for i in range(0,10):
    directory = 'dir' + str(i)
    subprocess.call(['mkdir', directory])
    subprocess.call(['cp', name, directory])

