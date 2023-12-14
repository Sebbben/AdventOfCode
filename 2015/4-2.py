import hashlib

key = "bgvyzdsv"

i = 1
while True:
    res = str(hashlib.md5((key + str(i)).encode()).hexdigest())
    if res[0:6] == "000000":
        print(i)
        exit()
    i += 1
