N = int(input())
a = 0
b = 1
i = 2
row = [a, b]
while i < N: 
    a, b = b, a + b
    row.append(b) 
    i += 1
print(row) 
for i in range(N): 
    if row[i] % 2 == 0: 
        row[i] = row[i] * 2 
    else: 
        row[i] = row[i] ** 2
print(row) 
row_max = max(row) 
print(max(row)) 
    
