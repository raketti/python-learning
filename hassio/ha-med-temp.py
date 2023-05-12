"""
Idea is to calculate the median temperature for the past week

I'll probably do it by:

1. Getting the current outside temperature from ATW Heat Pump sensor
  - This will be done by running the script once an hour
2. Sample size will be h = 24 / d = 7
3. Once we have a sample size of h * d + 1, we remove the first sample from the list
4. Then we calculate the median of the sample set
5. This value will be:
  - If supported added to a Home Assistant sensor
  - Read from this script
6. Then we use an automation to control the Target Heating Temperature (manly summer / winter)
"""