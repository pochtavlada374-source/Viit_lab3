def Summ(measurements):
    k = 0
    for num in measurements:
        k += num
    return k

def Minn(measurements):
    mini = measurements[0]
    for i in measurements:
        if i < mini:
            mini = i
    return mini

def Maxx(measurements):
    maxi = measurements[0]
    for i in measurements:
        if i > maxi:
            maxi = i
    return maxi

measurements = [7, 5, 6, 9, 12, 4, 2, 1]

print("Summ:", Summ(measurements), "/ sum():", sum(measurements))
print("Minn:", Minn(measurements), "/ min():", min(measurements))
print("Maxx:", Maxx(measurements), "/ max():", max(measurements))
