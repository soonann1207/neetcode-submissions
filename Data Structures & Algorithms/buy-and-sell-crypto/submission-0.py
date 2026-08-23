class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for purchase_date in range(len(prices)):
            for i in prices[purchase_date:]:
                if i - prices[purchase_date] > 0 and i - prices[purchase_date] > max_profit:
                    max_profit = i - prices[purchase_date]

        return max_profit
                

        