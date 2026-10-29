# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

import geometry
p = geometry.Point(1, 2)
c = geometry.Circle(5)

if p in c:
    print("Yes!")