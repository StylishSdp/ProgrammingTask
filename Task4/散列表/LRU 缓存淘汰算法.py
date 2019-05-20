# 参考https://shimo.im/docs/wiUMIdTR8Jsq7HO4/read

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity

    def set(self, key, val):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            #缓存满了，把用户最早访问的数据pop掉
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = val


    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

