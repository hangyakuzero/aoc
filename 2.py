l = []
k = []
flag = 0
flag1 = 0
with open("samp.txt", "r") as f1:
    lines = f1.read().splitlines()

    print(lines)
    for i in lines:
        k = i.split()
        for j in range(len(k)):
            k[j] = int(k[j])

        if sorted(k) == k or sorted(k, reverse=True) == k:
            # print(k)
            for n in range(len(k) - 1):
                diff = abs(k[n] - k[n + 1])
                if diff != 0 and diff <= 3:
                    flag += 1

            if flag == len(k) - 1:
                flag1 += 1
            flag = 0

        else:
            for i in range(len(k)):
                k.pop(i)
                if sorted(k) == k or sorted(k, reverse=True) == k:
                    # print(k)
                    for n in range(len(k) - 1):
                        diff = abs(k[n] - k[n + 1])
                        if diff != 0 and diff <= 3:
                            flag += 1

                if flag == len(k) - 1:
                    flag1 += 1
            flag = 0


print(flag1)
