## Interview Questions

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

ANSWER:
The runtime complexity of adding to an array to the front is O(n), as all elements have to be re-shifted in order to incorporate the new item being added at the front. Adding/removing at the end should be O(1) (especially if space had been pre-alloted)

Insertion at any point that is not the end would worst-case be O(n)

* What is the worse case scenario if you try to extend the storage size of a dynamic array?
ANSWER:
The worst case is O(n) as you need to effectively to replicate the original array as the number of operations grows.


Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?
ANSWER:

A blockchain is a structure that contains records of numerous transactions, a chain is made up of blocks. Each block has the following components:

Index - the number of the block in the chain, starting at 0 or 1, depending on the chain.
Timestamp - the time at which the block was created. This is not required, but is often useful.
Transactions - the monetary transactions, or any type of data, that is proofed by the block.
Proof - the proof for this block. Proof that work has been done.
Previous Hash - the hash of the previous block.
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
ANSWER:

Proof of Work is an arbitrarily difficult problem to solve. It essentially adds friction and prevents people from easily altering past transactions in the chain, as that altering past transactions in the chain would also require re-doing/regenerating valid Proofs of Work.
