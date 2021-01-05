# Primality-Testing-and-Factorisation
A collection of algorithms which will help when testing for primality of an integer, which will return some or all factors when the input is composite. 
Now also including files for encoding/ decoding and encrypting/ decrypting a message using RSA.

# RSA
RSA is an encryption system. It is highly secure due to the fact that factorisation of larger integers is difficult. The systems works by assigning a public key (e,n) and a private key (d,n) to each user. As the names would suggest (e,n) is visible to all, but it is specific to one user, so anyone intending to send an encrypted message to said user can do so. They can encrypt it by encoding the message using a public code, then they can take the encoded message to the power of the e and reduce this modulo n. Once they have encrypted the message they can happily send it to the intended receiver knowing that if it is intercepted then the data remains secure as only the receiver has the specific decryption key required. To decrypt the message you take the encrypted message to the power of d and reduce it modulo n, then after decoding the integer we are back to the original message.

As stated above, the factorisation of large integers is difficult. Due to this we let n=pq, where p and q are both prime. Since n only has two factors it is incredibly difficult to factor provided p,q are not 'predictable'. Ultimately, the more factors an integer has, the more likely you are to find one. Having said that, if n is the product of two primes but is even or the sum of it's digits are divisible by 3, then we know that n is divisible by 2 and 3 respectively with very little work to figure that out. For this reason we want to choose two large primes of a similar magnitude.
