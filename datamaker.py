# Import writer class from csv module
import random
from csv import writer
  
# List 
List=['Month','Month_count']
  
def add(List):

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('train.csv', 'a') as f_object:
   
        # Pass this file object to csv.writer()
        # and get a writer object.

        writer_object = writer(f_object)
  
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
  
        #Close the file object
        f_object.close()

add(List)
List=[]
for i in range(1,1001):
    r=random.choice([1,2,3,4,5,6,7,8,9,10,11,12])
    List.append(r)
    List.append(random.randint(5000,8000))
    add(List)
    List=[]
