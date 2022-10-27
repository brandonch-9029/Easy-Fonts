import os

directorylist = [item for item in os.listdir("tasks") if os.path.isdir(os.path.join("tasks", item))]

print(directorylist)