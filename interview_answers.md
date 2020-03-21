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

The blocks each contain a 
 
Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?
ANSWER:
