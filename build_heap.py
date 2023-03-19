# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data) // 2, -1, -1):
        siftdown(i,data,swaps)
        i-=1
    return swaps

def siftdown(i,data,swaps):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(data) and data[smallest] > data[l]:
        smallest = l
    if r < len(data) and data[smallest] > data[r]:
        smallest = r
    if smallest != i:
        data[i],data[smallest] = data[smallest],data[i]
        swaps.append([i,smallest])
        siftdown(smallest,data,swaps)

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    type = input()
    if "I" in type:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        file = "tests/" + input()
        with open(file, 'r', encoding="utf-8") as f:
            n = int(f.readline().strip())
            data = list(map(int,f.readline().strip().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
