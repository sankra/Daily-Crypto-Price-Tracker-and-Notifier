import threading
import time

def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")


# Create two threads
t1 = threading.Thread(target=task, args=("t1",)) 
t2 = threading.Thread(target=task, args=("t2",))

print('Before starting threads')
# Start the threads
t1.start()
t2.start()
print('after starting threads')

# Wait for both threads to complete
t1.join()
t2.join()

print("Both threads have finished execution")
print("after both threads have finished execution")