L = []
n = int(raw_input())
for i in range(0,n):
    a = raw_input().strip().split(" ")
    cmd = a[0]
    if cmd == "insert":
        L.insert(int(a[1]),int(a[2]))
    elif cmd == "print":
        print L
    elif cmd == "remove":
        L.remove(int(a[1]))
    elif cmd == "append":
        L.append(int(a[1]))
    elif cmd == "sort":
        L.sort()
    elif cmd == "pop":
        L.pop()
    elif cmd == "reverse":
        L.reverse()
    elif cmd == "count":
        L.count(int(a[1]))
