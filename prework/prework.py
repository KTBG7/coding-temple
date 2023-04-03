def hello_name(user_name):
    print("Hello_" + user_name);
hello_name('Kevin')
def first_odds():
    x = range(100)
    for n in x:
        if n%2 != 0:
            print(n)
first_odds()
def max_num_in_list(list):
    print(max(list))
    return max(list)
max_num_in_list({25, 548, 345})
def leap_year(year):
    if year%4 ==0:
        if year%100==0 and year%400==0:
            return True
        elif year%400==0 and year%100!=0:
            return True
    return False
print(leap_year(1900))
def is_consecutive(list):
    for n in range(len(list) -1):
        if list[n] + 1 == list[n+1]:
            continue
        return False
    return True
print(is_consecutive([1,2,3,5,5]))
