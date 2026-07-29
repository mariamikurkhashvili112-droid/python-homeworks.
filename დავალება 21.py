#დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და შეამოწმებს ეს რიცხვი არის თუ არა მარტივი

#შემდეგ ნაკადების გამოყენებით გაუშვით ეს ფუნქცია პარალელურად რომ შეამოწმოს შემდეგ ლისტში
#num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51] ყველა რიცხვი და დააბრუნოს პასუხი

import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

results = {}
lock = threading.Lock()

def check_prime_worker(num):
    status = is_prime(num)
    with lock:
        results[num] = status

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]
threads = []

for num in num_list:
    t = threading.Thread(target=check_prime_worker, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for num, prime in results.items():
    print(f"Number {num}: {'Prime' if prime else 'Not Prime'}")