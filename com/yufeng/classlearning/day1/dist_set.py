#!/usr/bin/python
#conding=utf-8
#dist set的使用，dist和map类似

dictionary={'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dictionary.get('Michael'))
dictionary.pop('Bob') #删除key和value

set_example = set([1, 2, 3, 3]) #重复元素在set中自动被合并
for set_node in set_example:
    print(set_node)
set_example.remove(3) #删除某个元素