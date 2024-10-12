import sys

filepath = sys.argv[1]
with open(filepath) as fp:
    lines = fp.readlines()

enriched = []
for line in lines:
    fragments = line.split(',')
    name = fragments[0]
    races = int(fragments[1])
    wins = int(fragments[2])
    classifications = int(fragments[3])

    # win_percentage = float(wins) / float(races)

    enriched += [(name, races, wins, classifications)]

results = sorted(enriched, key=lambda tup: tup[3], reverse=True)
for horse in results:
    print("%s: races %d, wins %d, classifications %d" % horse)
