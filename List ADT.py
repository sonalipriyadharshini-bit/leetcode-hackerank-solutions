if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            list1.insert(i,e)
        elif command[0] == "print":
            print(list1)
        elif command[0] == "remove":
            e = int(command[1])
            list1.remove(e) 
        elif command[0] == "append":
            e = int(command[1])
            list1.append(e)
        elif command[0] == "sort":
            list1.sort()
        elif command[0] == "pop":
            list1.pop()
        elif command[0] == "reverse":
            list1.reverse()           
