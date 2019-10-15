import zlib
a = "hello world!hello world!hello world!hello world!"
s = zlib.compress(a.encode("utf-8") )
print(s)
print(zlib.decompress(s))