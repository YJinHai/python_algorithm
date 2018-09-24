class SmallSum():
    def __call__(self, arr):
        self.arr = arr
        if not self.arr or len(self.arr)<1:
            return 0
        return self.merge_sort(0, len(self.arr)-1)

    def merge_sort(self, l, r):
        if l == r:
            return 0
        mid = l + ((r - l) >> 1)
        return self.merge_sort(l, mid) + self.merge_sort(mid + 1, r) + self.merge(l, mid, r)

    def merge(self, l, m, r):
        help = []
        p1 = l
        p2 = m + 1
        res = 0
        while p1 <= m and p2 <= r :
            res += (r - p2 + 1) * self.arr[p1] if self.arr[p1] < self.arr[p2] else  0
            if self.arr[p1] < self.arr[p2] :
                help.append(self.arr[p1])
                p1 += 1
            else :
                help.append(self.arr[p2])
                p2 += 1

        while p1 <= m :
            help.append(self.arr[p1])
            p1 += 1
        while p2 <= r :
            help.append(self.arr[p2])
            p2 += 1
        for i in range(len(help)):
            self.arr[l + i] = help[i]
        return res


small_sum = SmallSum()
print(small_sum([1, 2, 3]))

