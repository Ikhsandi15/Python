
def linear_search(n, search):
    flag = 0
    for num in n:
        if num == search:
            flag = 1
    if flag == 1:
        print("found")
    else:
        print("not found")

linear_search([1,2,3,4,5], 4)

