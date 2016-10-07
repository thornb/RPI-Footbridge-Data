#Data collection program by Brandon Thorne
#The data collected is the time and direction of RPI students crossing the footbridge

from datetime import datetime


#get name of csv file
print "Please enter the filename to save the csv data to."
filename = raw_input()

print "The filename is: " + filename

f = open(filename, 'w')


print "Press 1 if the student is crossing east, or 2 if the student is crossing west, and press enter. Press x to end the collection and save the file."


while True:
    key = raw_input()
    
    if key == "x":
        f.close()
        break
        
    elif key == "1":
        #save time and east
        time = str(datetime.utcnow())
        print time
        f.write("east, " + time + '\n')
        print "east"
        
    elif key == "2":
        #save time and west
        time = str(datetime.utcnow())
        f.write("west, " + time + '\n')        
        print "west"
        
print "Done with simulation"