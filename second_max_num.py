list1 = [100, 40, 49, 45, 75]
mx = max(list1)
secondmax = min(list1)
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]

print("Angka terbesar ke-2:", str(secondmax))
