import zlib, base64
text= zlib.decompress(base64.b64decode('eJyrzC9VSCxKVchITM5OTQEAJ08FNg=='))
print(text)
