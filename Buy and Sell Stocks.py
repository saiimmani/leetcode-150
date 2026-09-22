class Solution:

  def maxProfit(self, prices: list[int]) -> int:
    profit = 0
    min_p = prices[0]
    for price in prices:
      min_p = min(min_p, price)
      profit = max(profit, price - min_p)
    return profit
  
