#collection - special containers that make working with data easier
#counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a= 'aaaabbbbbcccc'
my_counter = Counter(a)
print(my_counter)#counts how many times each character appears
print(my_counter.most_common(3)[0][0])#gets the most frequent character
print(list(my_counter.elements()))#converts the counted elements into a list

Point = namedtuple('Point', ['x', 'y'])#creates a tuple with named fields
pt = Point(1, 2)
print(pt.x, pt.y)#accesses values using their names

#ordered dict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['a'] = 1
ordered_dict['d'] = 4
print(ordered_dict)#keeps the insertion order

#default dict
d= defaultdict(int)#returns 0 for missing keys
d['a'] =1
d['b'] =2
print(d['c'])#c is missing, so it returns 0

#deque
d= deque()
d.append(1)#adds an item to the right
d.append(2)
d.append(3)
d.appendleft(4)#adds an item to the left
print(d)

d.pop()#removes the rightmost item
d.popleft()#removes the leftmost item
d.clear()#removes all items

d.extendleft([1,2,3])#adds items to the left
print(d)

d.rotate(1)#moves the last item to the front
