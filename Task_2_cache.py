class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}
        self.usage_list = []

    def get(self, key):
        if key in self.cache_dict:
            self.update_usage(key)
            return self.cache_dict[key]

    @property
    def cache(self):
        # Возвращаем самый старый элемент
        oldest_key = self.usage_list[0]
        return oldest_key, self.cache_dict[oldest_key]

    @cache.setter
    def cache(self, new_elem):
        if len(self.cache_dict) >= self.capacity:
            # Удаляем самый старый элемент
            oldest_key = self.usage_list[0]
            self.usage_list.pop(0)
            del self.cache_dict[oldest_key]
        # Добавляем новый элемент
        key, value = new_elem
        self.cache_dict[key] = value
        self.usage_list.append(key)

    def update_usage(self, key):
        self.usage_list.remove(key)
        self.usage_list.append(key)

    def print_cache(self):
        print("LRU Cache:")
        for key in self.usage_list:
            print(f"{key} : {self.cache_dict[key]}")


if __name__ == '__main__':
    cache = LRUCache(3)

    cache.cache = ("key1", "value1")
    cache.cache = ("key2", "value2")
    cache.cache = ("key3", "value3")

    cache.print_cache()

    print(cache.get("key2"))

    cache.cache = ("key4", "value4")

    cache.print_cache()
