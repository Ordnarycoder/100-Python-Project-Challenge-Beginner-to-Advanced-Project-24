from queue import Queue

que =Queue(maxsize=4)

que.put(1)
que.put(2)
que.put(3)
que.put(4)
#methods
print("Full: ", que.full())
print("Removed Elements:")
print(que.get())
print(que.get())
print(que.get())
print(que.get())
print("Is it empty:", que.empty())
