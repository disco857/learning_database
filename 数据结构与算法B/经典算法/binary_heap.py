class BinaryHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def perc_up(self,i):
        while (i-1)//2>=0:
            father=(i-1)//2
            if self.heap[i] < self.heap[father]:
                self.heap[i], self.heap[father] = self.heap[father], self.heap[i]
            else:
                break
            i = father

    def perc_down(self,i):
        while 2*i+1<len(self.heap):
            sm_child=self.get_min_child(i)
            if self.heap[i] > self.heap[sm_child]:
                self.heap[i], self.heap[sm_child] = self.heap[sm_child], self.heap[i]
            else:
                break
            i = sm_child

    def get_min_child(self,i):
        left_child = 2*i+1
        right_child = 2*i+2
        if right_child < len(self.heap):
            if self.heap[left_child] < self.heap[right_child]:
                return left_child
            else:
                return right_child
        else:
            return left_child

    def insert(self,val):
        self.heap.append(val)
        self.perc_up(len(self.heap)-1)

    def remove(self):
        self.heap[0] , self.heap[-1] = self.heap[-1], self.heap[0]
        ans=self.heap.pop()
        self.perc_down(0)
        return ans

    def heapify(self, not_a_heap):
        self.heap = not_a_heap
        for i in range((len(not_a_heap)-1)//2,-1,-1):
            self.perc_down(i)

t=int(input())
heap=BinaryHeap()
heap.heapify([])
for _ in range(t):
    token=list(map(int,input().split()))
    if token[0]==1:
        heap.insert(token[1])
    elif token[0]==2:
        print(heap.remove())