def candies(n, arr):
    res = [1] * n
    for i in range(1, n):
        second = arr[i]
        first = arr[i - 1]
        
        if second > first:
            res[i] = res[i - 1] + 1

        # if second < first:
        #     # backtrack
        #     for j in range(i - 1, -1, -1):
        #         if arr[j] <= arr[j + 1]:
        #             break

        #         if res[j] > res[j + 1]:
        #             break
                
        #         if res[j] == res[j + 1]:
        #             res[j] = res[j] + 1
                    
    for i in range(n - 2, -1, -1):
        second = arr[i]
        first = arr[i + 1]
        
        if second > first and res[i] <= res[i + 1] + 1:
            res[i] = res[i + 1] + 1
        
    return sum(res)
                
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()