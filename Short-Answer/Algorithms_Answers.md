#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The reason this problem is O(n) is because intiallity a is compared to O(n^3), but considering that we add O(n^2) it becomes O(n).


b) O(n^2) - The reason this is Exponential is beacuse we have a nested for loop that is dependent on the size of N which is passed in.


c)O(n) - Although the code uses recursion, the problem is still reliant on how many bunnies are passed into it, cause it to be O(n)

## Exercise II

Answer: 

O(n)

We could use Binary search to find where the eggs break. We could slowly move up the floors from the middle, seeing if the egg broke, if it doesn't break from that floor, we continue to move up until the egg breaks, if it does break at the middle, we move down until the egg doesn't break and in turn we can find where that the floor above that is where the eggs start to break. This will use the least amount of eggs possible and in turn finding the where the eggs break in the least amount of time.


