from random import randint 
import time
import random
from math import sqrt
def brute_force(points):
    min=100000000000000000000000
    size=len(points)air=(points[i],points[j])
    return best_pair      


def closest_points(*args):
    from collections import deque
    import numbers

    points = list(args)
    if len(points) < 2 :
      raise NotImplementedError('At-least 2 points must be inserted' )

    for i in range(0,len(points)):
      if   isinstance(points[i][0], (int, long, float))==False  or isinstance(points[i][1], (int, long, float))==False or len(points[i])==False:
       raise NotImplementedError('The input must be a set of 2-d points' )

    points.sort(key=lambda x: x[0])

    box = deque()
    box.append(points[0])

    best_dist = sqrt(pow(points[1][1]-box[0][1],2)+pow(points[1][0]-box[0][0],2))
    left = 0
    i = 1
    best_pair = (points[0],points[1])

    while(i < len(points)):
       j = 0
       while left < i and points[i][0]-points[left][0] > best_dist:
          box.remove(points[left])
          left=left+1

       for j in range(len(box)):
           if best_dist != min(best_dist,sqrt(pow(points[i][1]-box[j][1],2)+pow(points[i][0]-box[j][0],2))):
              best_pair = (points[i],box[j])
              best_dist = min(best_dist,sqrt(pow(points[i][1]-box[j][1],2)+pow(points[i][0]-box[j][0],2)))
       box.append(points[i])
       i=i+1

    return best_pair

#Random Test one 
points = []
for i in range (1,100):
    points.append((random.uniform(1,1000),randint(1,1000)))
print points    

# This one Runs the sweep line  Algorithm 
start = time.clock()
print closest_points(*points)  
print time.clock() - start

# This one Runs the brute force Algorithm 
start = time.clock()
print brute_force(points)  
print time.clock() - start



# this is the plot of the results
import matplotlib.pyplot as plt
plt.scatter(*zip(*points),color='g')
plt.plot(*zip(*closest_points(*points)),color='k',marker='o')
plt.show()
