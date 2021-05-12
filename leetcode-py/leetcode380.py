# leetcode will import it directly
# outside leetcode, from ... import ... will save more space
# from random import randint
import random


class RandomizedSet:
    ''' the method one is slower
        if xx in list() are basically O(n) calling
    '''
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.item = []
    #
    # def insert(self, val: int) -> bool:
    #     """
    #     Inserts a value to the set. Returns true if the set did not already contain the specified element.
    #     """
    #     if val in self.item:
    #         return False
    #     self.item.append(val)
    #     return True
    #
    # def remove(self, val: int) -> bool:
    #     """
    #     Removes a value from the set. Returns true if the set contained the specified element.
    #     """
    #     if val in self.item:
    #         self.item.remove(val)
    #         return True
    #     return False
    #
    # def getRandom(self) -> int:
    #     """
    #     Get a random element from the set.
    #     """
    #     return random.choice(self.item)


    # method 2, save some time via hashmap
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # hashmap is O(1) when use xx in hashmap
        if val in self.item:
            return False
        self.item[val] = len(self.item)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.item:
            self.item.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.item.keys())

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()