import numpy as np

with open("inp.txt", "r") as f:
    data = f.read()


# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

    
chunks = data.split("\n\n")
seeds = list(map(int, chunks.pop(0).split(" ")[1:]))
newSeeds = []
for i in range(0,len(seeds), 2):
    newSeeds.append(list((seeds[i],seeds[i]+seeds[i+1]-1)))
seeds = newSeeds

mappings = {}

for mappingStr in chunks[0:]:
    mapping = mappingStr.splitlines()
    source, destination = mapping.pop(0).split(" ")[0].split("-to-")
    mappings[source] = {"dest": destination, "mappings":[]}
    for mapRange in mapping:
        dstStart, srcStart, length = list(map(int, mapRange.split(" ")))
        # mappings[source]["mappings"].append(lambda x: range(dstStart, dstStart+length-1)[range(srcStart,srcStart+length-1).index(x)] if (srcStart <= x < (srcStart+length-1)) else -1)
        mappings[source]["mappings"].append([dstStart-srcStart, [srcStart,srcStart+length-1]])
    
src = "seed"

def func(x, dstDiff, srcRange):
    # ("X: ", x, "Range: ", srcRange)
    if x[1] < srcRange[0] or x[0] > srcRange[1]: 
        return None, []
    
    newRanges = []
    if  x[1] > srcRange[1]:
        # print("Høyre")
        newRanges.append([srcRange[1]+1, x[1]])
        x[1] = srcRange[1]
    if x[0] < srcRange[0]:
        # print("Venstre", x)
        newRanges.append([x[0], srcRange[0]-1])
        x[0] = srcRange[0]
        # print("Venstre", x)print
            
            
    newX = [x[0]+dstDiff, x[1]+dstDiff]
    return newX, newRanges

    
# func = lambda x, dstRange,srcRange: dstRange[srcRange.index(x)] if x in srcRange else -1


while True:
    if src == "location": break
    dest = mappings[src]["dest"]
    print(src, dest)
    print()
    newSeeds = []
    while len(seeds):
        # print(seeds)
        seed = seeds.pop(0)
        foundOverlap = False
        for dstDiff, srcRange in mappings[src]["mappings"]:
            newSeed, newSeedRanges = func(seed, dstDiff, srcRange)
            if not newSeed is None:
                seeds += newSeedRanges
                newSeeds.append(newSeed)
                foundOverlap = True
        
        if not foundOverlap:
            newSeeds.append(seed)
                        
    seeds = newSeeds.copy()
    src = mappings[src]["dest"]

print(min((min(s) for s in seeds)))