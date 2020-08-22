from collections import defaultdict
class UnionFind:
    def __init__(self,names):
        self.parent={}
        for item in names:
            self.parent[item]=item
    def union(self,name_a,name_b):
        if name_a not in self.parent or name_b not in self.parent:
            return
        root_a=self.find(name_a)
        root_b=self.find(name_b)
        if root_a<root_b:
            self.parent[root_b]=root_a
        else:
            self.parent[root_a]=root_b
    
    def find(self,name):
        while self.parent[name]!=name:
            self.parent[name]=self.parent[self.parent[name]]
            name=self.parent[name]
        return name

class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        # 频率map
        freq_map = defaultdict(int)
        for name_freq in names:
            name, freq_str = (part.strip().strip(')') for part in name_freq.split('('))
            freq_map[name] = int(freq_str)
        # 初始化并查集
        uf = UnionFind(freq_map.keys())
        # 并操作
        for pair_str in synonyms:
            a, b = (name.strip().strip(')').strip('(') for name in pair_str.split(','))
            uf.union(a, b)
        result=[]
        res_map=defaultdict(int)
        for key,val in freq_map.items():
            par=uf.find(key)
            res_map[par]+=val
        for name, freq in res_map.items():
            result.append('{}({})'.format(name, freq))
        return result