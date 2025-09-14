#====================================================
# Filename: Prob2.py
# 
# Your name: Miles Fukuhara
# Who did you work with (if anyone)?: Looked back at slides
# Estimate for time spent (in hrs)?: <1
#====================================================

# Define your function here

def  divisible_by_six_or_seven(x,y):
    cnt = 0
    for i in range(x,y+1):
        if (not ((i % 6 == 0) and (i % 7 ==0))) and ((i % 6 == 0) or (i % 7 ==0)):
            print(i)
            cnt += 1
    return cnt

def backup():
    cnt = 0
    ncnt = 0
    for i in range(x,y+1):
        if (i % 6 == 0) and (i % 7 ==0):
            ncnt += 1
        elif (i % 6 == 0) or (i % 7 ==0):
            print(i)
            cnt += 1
    return cnt

# Boilerplate
if __name__ == '__main__':
    # Same basic testing here, but you should test MORE!
    count = divisible_by_six_or_seven(40,60)
    print(count)

