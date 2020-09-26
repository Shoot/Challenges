import base64

with open("obfuscated.txt", "r") as file:
	final = file.read()

# mikeSwift(...)
mike_swift_out = ''.join(final[::7])

# crypt(...)
fusc_data = list(mike_swift_out[3:])[::-1]
proc_data = []

for i in range(len(fusc_data)):
	if ''.join(fusc_data).startswith(str(i)[::-1]):
		fusc_data = fusc_data[len(str(i)):]
		proc_data.append(fusc_data.pop(0))

crypt_out = ''.join(proc_data)

# obfuscate(...)
refus = crypt_out[19:]
fusc = str(refus)[:-24]
bys = base64.b64decode(fusc.encode("utf-8")).decode("utf-8")

print(bys)