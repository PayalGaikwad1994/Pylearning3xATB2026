
try:
    file=open("payal.txt","r")
    print(file.read())
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()