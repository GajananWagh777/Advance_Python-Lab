import gc
import time

print("Garbage Collection Experiment")

# Automatic garbage collection
print("Garbage collection enabled:", gc.isenabled())

# Create objects
a = [1, 2, 3]
b = [4, 5, 6]

print("Objects created")

# Automatic garbage collection
del a
del b

print("Objects deleted")

# Manual garbage collection
start = time.time()

collected = gc.collect()

end = time.time()

print("Objects collected:", collected)
print("Time taken:", end - start, "seconds")

# Disable garbage collection
gc.disable()
print("Garbage collection disabled")

# Enable garbage collection
gc.enable()
print("Garbage collection enabled again")
