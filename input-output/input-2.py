input_val = input("Enter a number: ")
current_temp = 0

class MedianTemperature:

  def med_temp_out(self, current_temp):
    self.current_temp = current_temp
    current_temp = []
    current_temp.append(input_val)
    
    return(current_temp)

t = MedianTemperature(current_temp)
print(t)
#   print(temp_data) # list toimii, ei vaan saada arvoa lisättyä funktioon
#t = MedianTemperature(current_temp)
#print(t)
