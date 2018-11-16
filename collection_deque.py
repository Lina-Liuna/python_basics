#deque - Double ended queue
#A double-ened queue, or deque, supports adding and removing elements from either end of the queue.
#the more commonly used stacks and queues are degenerated forms of dequeues, where the input and outputs
#are restricted to a single end.

import collections

d = collections.deque('abcdefg')
print(d)
print(len(d))
print(d[0])
print(d[-1])

d.remove('c')
print(d)

dl = d
dl.extend('xyz')
print(dl)
dl.append('higk')
print(dl)

dl2 = collections.deque()
dl2.extendleft(range(6))
print(dl2)
dl2.appendleft(6)
print(dl2)
dl2.rotate(3)
print(dl2)
dl2.rotate(-3)
print(dl2)
dl2.reverse()
print(dl2)

d1 = collections.deque(maxlen=3)