import collections

class NestedIterator:
    def __init__(self, nested_list):
        
        # Flattening the nested list before iterating using dfs
        def flatten(nested):
            temp = []
            for i in nested:
                if i.isInteger():
                    temp.append(i.getInteger())
                else:
                    temp.extend(flatten(i.getList()))
            return temp
        
        self.nested_list = collections.deque(flatten(nested_list))
                                
    def next(self) -> int:
        return self.nested_list.popleft()
        
    def hasNext(self) -> bool:
         return self.nested_list