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

mappings = {}

for mappingStr in chunks[0:]:
    mapping = mappingStr.splitlines()
    source, destination = mapping.pop(0).split(" ")[0].split("-to-")
    mappings[source] = {"dest": destination, "mappings":[]}
    for mapRange in mapping:
        dstStart, srcStart, length = list(map(int, mapRange.split(" ")))
        
        # print(range(dstStart, dstStart+length))
        # mappings[source]["mappings"].append(lambda x: range(dstStart, dstStart+length-1)[range(srcStart,srcStart+length-1).index(x)] if (srcStart <= x < (srcStart+length-1)) else -1)
        mappings[source]["mappings"].append([range(dstStart, dstStart+length),range(srcStart,srcStart+length)] )
    
# print(mappings)
# print(79, mappings["seed"]["mappings"][0](79))
# dstStart = 52
# srcStart = 50
# length = 48
# n = 79
# print(range(dstStart, dstStart+length))
# print(range(srcStart,srcStart+length))
# print(range(dstStart, dstStart+length)[range(srcStart,srcStart+length).index(n)])
# print(srcStart <= n < (srcStart+length))
# print(range(dstStart, dstStart+length)[range(srcStart,srcStart+length).index(n)] if srcStart <= n < (srcStart+length) else -1)
# print(mappings["seed"]["mappings"][0](n))
# print([m(n) for m in mappings["seed"]["mappings"]])
# exit()

src = "seed"
func = lambda x, dstRange,srcRange: dstRange[srcRange.index(x)] if x in srcRange else -1

while True:
    if src == "location": break
    dest = mappings[src]["dest"]
    print(src, dest, seeds)
    newSeeds = []
    for i, seed in enumerate(seeds):
        seedMapping = [func(seed, dstRange, srcRange) for dstRange, srcRange in mappings[src]["mappings"]]
        # print(seed,seedMapping)
        seedMapping = max(seedMapping)
        newSeeds.append(seedMapping if seedMapping != -1 else seed)
    
    seeds = newSeeds
    src = mappings[src]["dest"]

print(min(seeds))