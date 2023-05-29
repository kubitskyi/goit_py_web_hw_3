import time
import multiprocessing


def factorize(*number):
    result = []
    for i in number:
        factors = []
        for j in range(1,i+1):
            if i % j == 0:
                factors.append(j)
        result.append(factors) 
    return result


def factorize_mp(*numbers):
    proc=multiprocessing.cpu_count()
    pool = multiprocessing.Pool(proc)
    result = pool.map(factorize_singl,numbers)
    pool.close()
    pool.join()
    return result

def factorize_singl(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors 

if __name__ == '__main__':
    start = time.time()
    a  = factorize(128, 255, 99999, 10651060)
    res = time.time() - start   
    print(res)


    st = time.time()
    b  = factorize(128, 255, 99999, 10651060)
    rst = time.time() - st
    print(rst)  

# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 
#              532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]