t = ("周杰伦", 11, ["footerball", "music"])

print(t.index(11))

print(t[0])

del t[2][0]
print(t)

t[2].append("coding")
print(t)