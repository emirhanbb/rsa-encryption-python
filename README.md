# RSA Algorithm Python
rsa encryption algorithm with python
How it works
The RSA algorithm ensures that the keys, in the above illustration, are as secure as possible. The following steps highlight how it works:

1. Generating the keys
Select two large prime numbers, xx and yy. The prime numbers need to be large so that they will be difficult for someone to figure out.
Calculate n = x * yn=x∗y.
Calculate the totient function; \phi(n) = (x-1)(y-1)ϕ(n)=(x−1)(y−1).
Select an integer ee, such that ee is co-prime to \phi(n)ϕ(n) and 1 < e < \phi(n)1<e<ϕ(n). The pair of numbers (n,e)(n,e) makes up the public key.
Note: Two integers are co-prime if the only positive integer that divides them is 1.

Calculate dd such that e.d = 1e.d=1 modmod \phi(n)ϕ(n).
dd can be found using the extended euclidean algorithm. The pair (n,d)(n,d) makes up the private key.

2. Encryption
Given a plaintext PP, represented as a number, the ciphertext CC is calculated as:

C = P^{e}C=P
​e
​​  modmod nn.

3. Decryption
Using the private key (n,d)(n,d), the plaintext can be found using:

P = C^{d}P=C
​d
​​  modmod nn.
