from pprint import pprint


def bank(n):
    return [x for x in range(n)]

def foo(banks):
    n = len(banks)    
    if (n%4 and n>2) and n!=2:
        raise Exception('bank count must be 2^n')
    
    banks.sort() # generate the first row, in case the list is not in asc order
    ans = [banks]
    length_of_ans = 1
    
    half = int(n/2)
    sum_of_two = min(banks)+max(banks)
    
    # it's a skew symmetric matrix so just getting the first half is ok
    # generate the upper half
    for i in range(1,half):
        prev_row = ans[-1]
        row = []
        for j in range(length_of_ans):
            row.append(ans[-length_of_ans+j][length_of_ans])
        for k in range(half-length_of_ans):
            row.append((-1)**(length_of_ans+1)+prev_row[2*k+1+length_of_ans])
            row.append((-1)**length_of_ans+prev_row[2*k+length_of_ans])
        for k in range(length_of_ans-1,-1,-1):
            row.append(sum_of_two - row[k] )
        ans.append(row)
        length_of_ans += 1
        
    # based on the upper half, rotate the matrix by 180 degree
    
    for i in range(half-1,-1,-1):
        row = ans[i][:]
        row.reverse()
        ans.append(row)
    
    return ans

ans = foo(bank(2))
pprint(ans)
ans = foo(bank(4))
pprint(ans)
ans = foo(bank(8))
pprint(ans)
ans = foo(bank(16))
pprint(ans)
ans = foo(bank(32))
pprint(ans)

        
    