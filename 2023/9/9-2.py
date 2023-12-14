with open("inp.txt", "r") as f:
    data = f.read().splitlines()

# data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".splitlines()

tot = 0

for line in data:
    seq = list(map(int, line.split()))
    seqs = [seq]
    while not all(x == 0 for x in seqs[-1]):
        seqs.append([seqs[-1][i]-seqs[-1][i-1] for i in range(1,len(seqs[-1]))])


    for i in range(len(seqs)-2, -1, -1):
        seqs[i] = [seqs[i][0]-seqs[i+1][0]] + seqs[i]
    
    # print(seqs)
    tot += seqs[0][0]

print(tot)
        
    

    

# for line in data:
#     seq = list(map(int, line.split()))[::-1]
#     seqs = [seq, [seq[1]-seq[0]]]
#     while seqs[-1][0] != 0:
#         num2NdLevel = len(seqs[1])
#         seqs[1].append(seqs[0][num2NdLevel+1]-seqs[0][num2NdLevel])
#         for i in range(1,len(seqs)):
#             if len(seqs[i]) == 2:
#                 seqs.append([seqs[i][1]-seqs[i][0]])
#             else:
#                 seqs[i+1].append(seqs[i][-2]-seqs[i][-1])
    
#     print(line, seqs)
#     break