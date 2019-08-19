def main():
    def result(arr):
        arr.append(0)
        arr.append(0)
        for x in range(len(arr) - 3, -1, -1):
            if arr[x] + arr[x + 2] > arr[x + 1]:
                arr[x] += arr[x + 2]
            else:
                arr[x] = arr[x + 1]
        return arr[0]

    nb = int(input())
    for c in range(nb):
        n = int(input())
        ma = list(map(int, input().split()))
        print("Case %s: %s" % (c + 1, result(ma)))


main()
