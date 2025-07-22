import random
import time

class PrimeChecker:
    def exponentiate(self, m:int, y: int, mod: int) -> int:
        x = 1
        while y:
            if y & 1:
                x = x * m % mod
            m = m * m % mod
            y >>= 1
        return x
    
    def get_bases(self, n: int, k: int) -> list[int]:
        if n < 1373653:
            # All primes have been shown to be proven true using the below bases for Rabin-Miller -> primes < 1373653
            return [2, 3]
        if n < 3317444400000000000:
            # All primes have been shown to be proven true using the below bases for -> primes < 3317444400000000000
            return [2, 3, 5, 7, 11, 13, 17]
        bases = set()
        while len(bases) < k:
            bases.add(random.randrange(2, n-2))
        return list(bases)

    def check(self, p: int) -> bool:
        if p in (2, 3, 5): return True
        if p < 5 or p & 1 == 0: return False

        # generate bases that we can use to determine primality
        randomBases = self.get_bases(p, 20)

        # We are looking for the square of 1 mod p, within the range -> [0, s-1] for (p-1)^(2^s * d), where p is the prime we are currently checking, s is how many times we can factor out 2 from p-1, d is the remainder when the least significant bit is 1.
        sq1_mod_p = p-1
        d = p-1
        log2 = 0
        while d & 1 == 0:
            log2 += 1
            d >>= 1
        # we now have factored out all the 2's -> in the variable log2, d is the odd remainder

        for base in randomBases:

            root = self.exponentiate(base, d, p)
            # if the base raised to the power of the odd remainder mod p is 1, then its already the trivial root and the rest of sequence is 1^2, which is 1's. We continue to next base
            if root == 1 or root == sq1_mod_p: continue
            # Now we check the root raised to the power of 2's in the range [0, log2-1], mod p ofcourse, if we find the square of 1 mod p, we continue with the number as a possible prime, if we dont find square within range, return False Early
            # The nontrivial root is always p-1,  since (p-1) * (p-1) = p^2 - 2p + 1 -> p^2 mod p = 0, - 2p mod p = 0,... [1 mod p = 1]
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


