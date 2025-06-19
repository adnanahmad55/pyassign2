from typing import List

def compute_squares(nums: List[int]) -> List[int]:
   
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

print(compute_squares([1, 2, 3, 4, 5]))
print(compute_squares([6, 7, 8]))
