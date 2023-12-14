from PIL import Image

with open("9.txt") as f:
    cont = [[int(i) for i in list(x)] for x in f.read().splitlines()]


img = Image.new("RGB",(len(cont),len(cont[0])),(0,0,0))

for i in range(len(cont)):
    for j in range(len(cont[0])):
        colr = int((cont[i][j]/9)*255)
        # colr = 255 if cont[i][j]==9 else 0
        img.putpixel((i,j),(colr,colr,colr))

# for y in range(0,len(cont)):
#     for x in range(0,len(cont[y])):
#         low = True
#         for dx in [1,-1]:
#             if 0<=x-dx<=len(cont[y])-1:
#                 if cont[y][x]>=cont[y][x-dx]:
#                     low = False
#                     break
#         if not low:
#             continue
#         for dy in [1,-1]:
#             if 0<=y-dy<=len(cont)-1:
#                 if cont[y][x]>=cont[y-dy][x]:
#                     low = False
#                     break
#         if low:
#             print(x,y,cont[y][x])
#             img.putpixel((x,y),(255,255,255))


img.show()