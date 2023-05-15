## Things to do
Idea is to calculate the median temperature for the past week

Probably do it by:

- [x] Getting the current outside temperature from ATW Heat Pump sensor
- [ ] Create sample size h = 24 / d = 7
- This will be done by running the script once an hour
- [ ] After sample size is h * d + 1, remove the first sample from the list
- [ ] Then we calculate the median of the sample set
- [ ] Add median value to a Home Assistant sensor
- [ ] Read median value from sensor
- [ ] Use an automation to control the Target Heating Temperature (manly summer / winter)
