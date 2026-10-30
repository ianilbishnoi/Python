from threading import Thread

def square_numbers():
    for i in range(100):
        i*i

if __name__ == '__main__':
    threads=[]
    nums_threads=10

    #creating threads
    for i in range(nums_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    #starting all threads
    for thread in threads:
        thread.start()

    #waiting for all threads to finish
    for thread in threads:
        thread.join()

    print("End Main")
