import random
import time

class PrimeChecker:
    def exponentiate(self, x:int, y: int, mod: int) -> int:
        m = x
        x = 1
        while y:
            if y & 1:
                x = x * m % mod
            m = m * m % mod

            y >>= 1
        return x
    
    def get_random_bases(self, n: int, k: int) -> list[int]:
        if n-4 < k:
            return list(range(2, n-2))
        
        bases = set()
        while len(bases) < k:
            bases.add(random.randrange(2, n-2))
        return list(bases)

    def check(self, p: int) -> bool:
        if p in (2, 3, 5): return True
        if p < 5 or p & 1 == 0: return False

        randomBases = self.get_random_bases(p, 20)

        sq1_mod_p = p-1
        for base in randomBases:
            d = p-1
            log2 = 0
            while d & 1 == 0:
                log2 += 1
                d >>= 1

            root = self.exponentiate(base, d, p)

            if root == 1 or root == sq1_mod_p: continue

            for _ in range(log2-1):
                root = (root * root) % p
                if root == sq1_mod_p: break
            else:
                return False
        return True
    


print(1 / (2 ** 20))
## example usage
checker = PrimeChecker()

first_1000_primes = [i for i in range(2, 1001) if checker.check(i)]

print(first_1000_primes)

# Benchmark ot two large primes
start = time.time()
print(checker.check(1000000000061))
end = time.time()
print(end-start)


start = time.time()
print(checker.check(1000000000039))
end = time.time()
print(end-start)


