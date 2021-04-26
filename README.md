# RSA Algorithm Python
rsa encryption algorithm with python
RSA logic is based on the fact that it is more difficult to factorize an integer than to multiply it by new numbers. A base value consisting of multiplying two prime numbers that are large enough and different from each other is obtained. And other key parameters are also derived from the same two primes. Therefore, if the base value is factorized, the private key is compromised. Therefore, if we double or triple the key size, the encryption power increases exponentially (2).

His work is as follows,

Two prime numbers are selected. It is important for security that these numbers are large. Let's call these two numbers p and q.
For Keys, the base value must be calculated. If we say N to the base value, this value can be calculated as n = p*q.
the totient function is calculated for the value n. Since both factors are prime, the totient function of N exists as φ(n) = (p-1)(q-1).
If we call our Public key value e, a prime number must be selected from the range 1< e <φ(N) to find E. our E value is now our public key value.
If we say D to our Private key value, the value d is calculated as d*e = 1 mod (n).
