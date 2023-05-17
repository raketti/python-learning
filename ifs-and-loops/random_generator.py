outputFile = "ifs-and-loops/temp_data.txt"
h = 24              # Hours
d = 7               # Days
sampleSize = h * d  # Calculate the sample size
  
# Test wit a random number generator to get some data
def random_generator():
  import random

  for count in range(1):
    # So we have winters in Finland, let's generate some colder temperatures also
    i = random.randint(-30, 30)
    f = open(outputFile, 'a')
    f.write((str(i) + "\n"))
    f.close()

random_generator()

# Keep data until we have enough samples,
# If sampleSize is met, start removing old data
def removeFirstLine():

# Count the number of lines
  with open(outputFile, 'r') as lc:
    line_count = sum(1 for line in lc)

# If we have enough samples, we remove the first entry
  if line_count >= sampleSize:
    with open(outputFile, 'r+') as fr:
      
        # read an store all lines into list
        lines = fr.readlines()
        
        # move file pointer to the beginning of a file
        fr.seek(0)
        
        # truncate the file
        fr.truncate()

        # start writing lines except the first line
        fr.writelines(lines[1:])
  else:
    print("Not enough samples, sample size:", line_count, "Required:", sampleSize)

removeFirstLine()

def calculateAverage():
  # Initiate lists
  str_list = []
  int_list = []
  
  # Count the number of lines
  with open(outputFile, 'r') as lc:
    line_count = sum(1 for line in lc)

  # Get the values to a list  
  with open(outputFile) as f:
    str_list = [line for line in f]

  # remove new line characters
  with open(outputFile) as f:
    str_list = [line.rstrip() for line in f]

  # Convert string to int
  for x in str_list:
    int_list.append(int(x))

  # Calculate the average from the samples
  sumOfNums = 0
  count = 0
  for number in int_list:
    sumOfNums += number
    count += 1
    average_temp = sumOfNums / count

  # Round the number to two digits
  avg_rounded = round(average_temp, 2)
  
  # Convert to a string for Home Assistant
  avg_str = str(avg_rounded)
  
calculateAverage()

# Now that the different functions are working
# I need to probably refactor the code so that we can remove unnecessary duplicates
# And see how this will run in Home Assistant 