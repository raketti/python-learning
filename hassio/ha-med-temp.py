#Idea is to calculate the median temperature for the past week

#Probably do it by:

#1. Getting the current outside temperature from ATW Heat Pump sensor
#  - This will be done by running the script once an hour
#2. Sample size will be h = 24 / d = 7
#3. Once we have a sample size of h * d + 1, we remove the first sample from the list
#4. Then we calculate the median of the sample set
#5. This value will be:
#  - If supported added to a Home Assistant sensor
#  - Read from this script
#6. Then we use an automation to control the Target Heating Temperature (manly summer / winter)

# Test that we get the entity data

#--------------------------------------------------------------------------------------------------
# Get the state for the entity specified in the Automation Action
#--------------------------------------------------------------------------------------------------

inputEntity = data.get('entity_id')
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state

if inputEntity is None:
  logger.warning("===== entity_id is required if you want to set something.")
else:
  logger.warning("===== Got Entity ID: %s", inputEntity)
  
if inputState is None:
  logger.warning("===== Fail - inputState: %s", inputState)
else:
  logger.warning("===== Success - inputState: %s", inputState)

if inputStateObject is None:
  logger.warning("===== Fail - inputStateObject: %s", inputStateObject)
else:
  logger.warning("===== Success - inputStateObject: %s", inputStateObject)