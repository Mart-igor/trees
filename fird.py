from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for price in range(len(prices)):
            for discount in prices[price + 1:]:
                if prices[price] >= discount:
                    answer.append(prices[price] - discount)
                    break
            if price != len(answer) - 1:
                answer.append(prices[price])
        return answer
    

if __name__ == '__main__':
    s = Solution()
    print(s.finalPrices([1,2,3,4,5]))