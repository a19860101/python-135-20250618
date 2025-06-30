t = (12,52,63,32,31,12,12,12)

# print(len(t))

# print(t.index(12))

# print(t.count(12))

# t = sorted(t)

# t = reversed(t)


# print(t)

gps = ('121.3', '23.5')

# lon = gps[0]
# lat = gps[1]

# unpack
lon, lat = gps

print(lon,lat)

q = reversed(gps)

for qq in q:
    print(qq)