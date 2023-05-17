outputFile = "ifs-and-loops/temp_data.txt"
h = 24              # Hours
d = 7               # Days
sampleSize = h * d  # Calculate the sample size
  
# Test wit a random number generator to get a 
def random_generator():
  import random

  for count in range(1):
    
    i = random.randint(1, 25)
    
    f = open(outputFile, 'a')
    f.write((str(i) + "\n"))
    f.close()

random_generator()

# Keep data until we have enough samples,
# if sampleSize is met, start removing old data
def removeFirstLine():

# Count the number of lines
  with open(outputFile, 'r') as lc:
    line_count = sum(1 for line in lc)
    print('Total Number of lines:', line_count)

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
    print("Not enough samples, will keep data")
removeFirstLine()