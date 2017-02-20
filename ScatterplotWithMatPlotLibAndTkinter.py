#Program made by mchl02
#WARNING PROGRAM USES PYTHON 2.7
import matplotlib 
import fileinput 
matplotlib.use('TkAgg')


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from math import *

#All the lists here
first_column = []
second_column = []
third_column = []
fourth_column = []
fifth_column = []
new_second_column = []
new_fifth_column = []

"""
You will have to change the filename by dragging the pr5-input-data.txt you downloaded
to terminal or command line and copy the new file name. Next you will have to replace the 
file_name below with the copied version of your new file name. 

"""
#For this code the x axis is second column
#The Y axis is the fifth column
file_name = "/Users/kclee/Dropbox/pyprac/pr5-input-data.txt" 
#Using a counter to find the legnth
legnth_Of_The_First_Column = 0
#Parsing
print "Showing data getting parsed"
for data in fileinput.input([file_name]):
    paring = data.split()
    print len(paring)
    first_column.append(int(paring[0]))
    #Prints the whole first column by using for loop and parsing 
    #Showing example of how I got the other columns
    print "1st =", first_column
    #same thing to the other columns
    second_column.append(int(paring[1]))
    third_column.append(float(paring[2]))
    fourth_column.append(float(paring[3]))
    fifth_column.append(float(paring[4]))
    legnth_Of_The_First_Column = legnth_Of_The_First_Column + 1
		
	
print "len =", (legnth_Of_The_First_Column)

print "1st col =", (first_column)

#This prints all the rows
for x in range(len(first_column)):
	print "All rows =", first_column[x], " ", second_column[x], " ", third_column[x]," ", fourth_column[x]," ", fifth_column[x]


#second_column is the x-axis and the fifth_column is the y-axis
#This code is for finding the median
Placer_For_The_Xaxis = 0
Placer_For_The_Yaxis = 0
string_version_of_Legnth_Xaxis = ""
string_version_of_Legnth_Yaxis = ""
Legnth_Of_Xaxis = len(second_column)
Legnth_Of_Yaxis = len(fifth_column)

"""
Possible ways to find the median. I try to append everything 
"""
#Adding up all the numbers in the X axis or second column
for all_possible_numbersx in second_column:
	Placer_For_The_Xaxis = Placer_For_The_Xaxis + all_possible_numbersx

#Adding up all the numbers in the Y axis or fifth column
for all_possible_numbersy in fifth_column:
	Placer_For_The_Yaxis = Placer_For_The_Yaxis + all_possible_numbersy

#Median is all numbers added divided by the legnth of the list
The_Mean_Of_Xaxis = (Placer_For_The_Xaxis)/(Legnth_Of_Xaxis)
The_Mean_Of_Yaxis = (Placer_For_The_Yaxis)/(Legnth_Of_Yaxis)
	
print "The mean of the X axis is:",(The_Mean_Of_Xaxis)
print "The mean of the Y axis is:",(The_Mean_Of_Yaxis)
#The code for finding the median ends here

#The code for finding the variance starts here

Placer2_for_the_xaxis = 0
Placer2_for_the_yaxis = 0
string_version_of_Placer2X = ""
string_version_of_Placer2y = ""

#Below this is all the fomula for finding the variance
"""
Variance = (First number - median)^2 + (Second number - median)^2 and so on / (36 or legnth_Of_The_Columns)
"""
#Used to find the variance of the X axis
for Matthewx in second_column:
	Placer2_for_the_xaxis = Matthewx - The_Mean_Of_Xaxis
	#Square the number because of variance
	new_second_column.append(Placer2_for_the_xaxis*Placer2_for_the_xaxis)
print "This is the new second column or X axis" ,new_second_column	
#Prints the elements in the new second column
print "Printed in a for loop"
for xtra__ in new_second_column:
	print xtra__
#Used to add up all the numbers
total_finding = 0
for finding in new_second_column:
	total_finding = finding + total_finding
	#Prints the total of the numbers
	print total_finding

print "This is the total for the x axis" ,total_finding
"""I am using legnth of first column even when x-axis is the second column 
because all the columns have the same legnth"""
This_is_the_answer_for_x_axis = total_finding/legnth_Of_The_First_Column
print "This is the variance of the X axis" ,This_is_the_answer_for_x_axis

#Used to find the variance of the Y axis
for Matthewy in fifth_column:
	Placer2_for_the_yaxis = Matthewy - The_Mean_Of_Yaxis 
	#Square the number because of variance
	new_fifth_column.append(Placer2_for_the_yaxis*Placer2_for_the_yaxis)

print "This is the new fifth column" ,(new_fifth_column)

total_findingy = 0
for findingy in new_fifth_column:
	total_findingy = findingy + total_findingy
	print total_findingy


This_is_the_answer_for_y_axis = total_findingy/legnth_Of_The_First_Column
print This_is_the_answer_for_y_axis

#Prints all the things found	
print """For this project I am using the second column as the x axis
and using the fifth column as the y axis. On the matplotlib graph the x axis
only have 1,2,3,4 and etc because matplotlib could not write all the zeroes
needed for the x axis. """
print "This is the second column" , (second_column)
print "This is the fifth column" , (fifth_column)
print "The mean of the X axis is:",(The_Mean_Of_Xaxis)
print "The mean of the Y axis is:",(The_Mean_Of_Yaxis)
print "This is the standard variance of the X axis" ,This_is_the_answer_for_x_axis
print "This is the standard variance of the Y axis" ,This_is_the_answer_for_y_axis

#Below is all the tkinter stuff

root = Tk.Tk()
root.wm_title("Scatter Plot for TKinter")

f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)

a.scatter(second_column,fifth_column)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
toolbar = NavigationToolbar2TkAgg( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
label1 = Tk.Label(root, text = "The Mean of the X-axis is:")
label1.pack()		
label2 = Tk.Label(root, text = The_Mean_Of_Xaxis)
label2.pack()
label3 = Tk.Label(root, text = "The Mean of the Y-axis is:")
label3.pack()
label4 = Tk.Label(root, text = The_Mean_Of_Yaxis)
label4.pack()
label5 = Tk.Label(root, text = "This is the standard variance for the x-axis:")		
label5.pack()
label6 = Tk.Label(root, text = This_is_the_answer_for_x_axis) 
label6.pack()
label7 = Tk.Label(root, text = "This is the standard variance for the y-axis:")
label7.pack()
label8 = Tk.Label(root, text = This_is_the_answer_for_y_axis)
label8.pack()


Tk.mainloop()