

import itertools

def test(cases, cn = 1):
    cnt = 0
    while cnt < cn and cnt < len(cases):
        print "case:", cnt + 1 
        ret = ans(*cases[cnt])
        print "\n\tret:", ret
        print "-" * 10
        cnt += 1

def factor(n):
    ret = []
    cnt = 1
    while cnt * cnt <= n:
        if n % cnt == 0:
            ret.append(cnt)
            ops = n / cnt
            if cnt != 1 and ops != cnt:
                ret.append(ops)
        cnt += 1
    return ret

def binsearch(nums, n, l, h):  # nums is sorted array
    if h < l:
        return False
    mid = (l + h)/ 2
    if n < nums[mid]:
        return binsearch(nums, n , l, mid - 1)
    elif n > nums[mid]:
        return binsearch(nums, n , mid + 1, h)
    else:
        return True
    

def linsearch(nums, b):  # nums is sorted array
    for j in xrange(len(nums)):
        if b > nums[j]:
            continue
        elif b < nums[j]:
            return (j, False)
        else:
            return (j, True)
    return (len(nums), False)

def list2dic(nums):
    dic = {}
    for i in nums:
        if dic.has_key(i) == False:
            dic[i] = 0
        dic[i] = dic[i] + 1
    return dic

def list2dic_bool(nums):
    return { item:True for item in nums }

def bfs(a, index, hist):
    q = [index]  # init
    while len(q) != 0:
        i = q.pop(0)
        # do operation
        if hist[i] == 1:
            continue
        hist[i] = 1

        # post
        for j in xrange(len(a[i])):
            if a[i][j] == 1 and i != j:
                q.append(j)


def iter_combination(table, n):
    return itertools.combinations(table, n)

def iter_permutations(table, n):
    return itertools.permutations(table, n)

def dist(a,b):
    x_diff = abs(b[0] - a[0])
    y_diff = abs(b[1] - a[1])
    return x_diff * x_diff + y_diff * y_diff

def boomerangs(tup):
    if dist(tup[0], tup[1]) == dist(tup[0], tup[2]):
        return True
    else:
        return False

def isPalindrome(x):
    if x < 0:
        return False
    px = 0
    tmp = x
    while tmp != 0:
        r = tmp % 10
        tmp = tmp / 10
        px = (px * 10) + r
    return px == x

def sum_equ(ls):
    x, c = 0, 0
    for n in ls:
        if n == "":
            continue
        if "x" in n:
            if len(n) == 1:
                x += 1
            elif len(n) == 2 and n[0] == "-":
                x -= 1
            else:
                x += int(n[:-1])
        else:
            c += int(n)
    return x, c

def ans(x):
    left, right = x.split("=", 1)
    left = left.replace("-", "+-")
    right = right.replace("-", "+-")
    lls = left.split("+")
    rls = right.split("+")
    print lls
    lx, lc = sum_equ(lls)
    print lx, lc
    print rls
    rx, rc = sum_equ(rls)
    print rx, rc
    if lx == rx and lc == rc:
        return "Infinite solutions"
    else:
        if lx - rx == 0:
            return "No solution"
        val = (rc - lc) / (lx - rx)
        return "x=%s"%val

cases = [
        ["x+5-3+x=6+x-2"],
        ["x=x"],
        ["x=x+2"],
        ["-x=-1"]
]
test(cases,4)

