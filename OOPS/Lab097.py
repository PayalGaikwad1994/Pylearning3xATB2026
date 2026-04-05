#File IO

try:
    file= open("poyal.txt","r")
    pay=file.read()
    print(pay)

except FileNotFoundError as fnfe:
    print("File not found,Please check the path")
finally:
    print("Executed")
    try:
        file.close()
    except NameError as ne:
        print(ne)
