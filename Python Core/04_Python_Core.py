# dictionary -> {key:value} pair
dic = {
  "namme":"abhishek",
  "age":19,
  "subject":"computer science"
}
print(dic.keys())
print(dic.values())
print(dic["age"])
print(dic.get("age"))

for valuess in dic.values():
  print(valuess)

print(dic.items())


# methods  ordered way
ep = {
  1:10,
  2:13,
  3:9,
  5:12,
  4:14,
  6:15,
  7:8
}
ep2 = {
  8:10,
  9:12,
  10:16,
  11:13,
  12:14
}
print(ep)
ep.