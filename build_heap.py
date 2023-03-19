# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    i = 0
    heap = False
    temp=True
    while heap == False:
        l = 2*i+1
        r = 2*i+2
        print(data)
        #print("Index: "+str(i))
        #print("Right: "+str(r)+" ;Left: "+str(l))
        smallest = i
        if l < len(data):
            if data[i] > data[l]:
                smallest = l
        if r < len(data):
            if data[i] > data[r]:
                smallest = r
        #print("Smallest: "+str(smallest))
        if smallest != i:
            temp=False
            data[i],data[smallest] = data[smallest],data[i]
            swaps.append([i,smallest])
        if i==len(data):
            if temp==True:
                heap=True
            else:
                i = 0
                temp=True
        else:
            i+=1
    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    type = input()
    if "i" in type:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        file = "/tests" + input()
        with open(file, 'r') as f:
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
