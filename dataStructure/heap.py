class Heap:
    def __init__(self,data):
       self.heap_array = list()
       #heap은 인덱스 1부터 사용하기 때문에 0에 None
       self.heap_array.append(None) 
       self.heap_array.append(data)


    #데이터를 올릴수 있는지 검사한다
    def move_up(self, inserted_idx):   
     if(inserted_idx <= 1):
        return False

     parent_idx = inserted_idx // 2
     
     if(self.heap_array[inserted_idx] > self.heap_array[parent_idx]):
        return True
     else:
        return False   

    #맨 아래 넣어줌 
    def insert(self,data):
        #사이즈 없을시 초기화
        if(len(self.heap_array) == 0):
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        #추가한 노드의 인덱스 저장 
        inserted_idx = len(self.heap_array)-1   
        #부모노드와 검사, 값이 크면 swap
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            #swap 방법  1, 2 = 1, 2 : 1(후)을 1(전)에 대입, 2(후)를 2(전)에 대입을 동시에 
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True


heap = Heap(2)
heap.insert(3)
heap.insert(8)
heap.insert(10)
print(heap.heap_array)

