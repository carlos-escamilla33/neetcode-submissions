class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            distance = 0
            for j in range(i + 1, len(temperatures)):
                distance += 1
                if temperatures[j] > temperatures[i]:
                    break
            else:
                distance = 0
            result.append(distance)

        return result



"""
We have an array of integers representing temperatures. In the return array result the value in each position is the number of days after the ith day
 temperatures = [30,38,30,36,35,40,28]
 
init a result array
init a stack with the temps

for the temp in the temp array:
    while the stack is not empty

"""
        