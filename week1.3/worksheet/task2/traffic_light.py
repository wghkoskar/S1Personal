"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

associatedLingerTime = states.get(state)
stateIndex = 0
currentDuration = 0

for i in range(maxtime + 1): # 
    if associatedLingerTime == currentDuration: # Checks whether the lingering has been going on enough
        currentDuration = 1 # Resets the current duration
        stateIndex += 1 # Increases state index by 1 to go to the next one
        state = list(states.keys())[stateIndex % len(states)] # Converts the keys to a list and grabs the state index, the % ensures it never goes higher than the length of the list
        associatedLingerTime = states.get(state) # Updates the new linger time
    else:
        currentDuration += 1
    print(f"Time {i:03} State {state}")

