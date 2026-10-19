
# function implementation

def rectangle_area(height, width ):  # define suitable input data
    area = height * width         # implement the function
    return area      # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(1, 2 )}")   # provide suitable data matching your inputs

def evenRange (end):
    rangeOfEven = []
    for i in range(end):
        if i % 2 == 0:
            rangeOfEven.append(i)
    return rangeOfEven
print(evenRange(15))

def averageList(rawList):
    average = sum(rawList) / len(rawList)
    return average
print(averageList([1, 2, 3, 4]))