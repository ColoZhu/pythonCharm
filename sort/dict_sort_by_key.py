from operator import itemgetter

# Python对字典按照key排序

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

print("按fname升序")
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)

print("按uid升序")
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

print("最小的uid")
print(min(rows, key=itemgetter('uid')))
