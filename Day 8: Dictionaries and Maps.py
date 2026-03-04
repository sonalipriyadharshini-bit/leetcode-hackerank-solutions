# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}
for _ in range(n):
        entry = input().split()
        phone_book[entry[0]] = entry[1]
while True:
    try:
        name = input()
          
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
            
    except EOFError:
        
        break
