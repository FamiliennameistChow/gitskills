a = "IX"


dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# print(len(s))
sum = dict[a[0]]
for j in range(len(a)-1):
    if dict[a[j]] >= dict[a[j+1]]:
        sum += dict[a[j+1]]
    else:
        sum -= dict[a[j+1]]
print(sum)


