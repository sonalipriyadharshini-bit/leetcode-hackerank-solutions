class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            # Convert the number to a string to access each digit
            for digit in str(num):
                # Convert the digit back to an integer and add it to our list
                answer.append(int(digit))
        return answer
