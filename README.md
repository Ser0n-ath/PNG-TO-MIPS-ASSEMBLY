# PNG-TO-MIPS-ASSEMBLY
A python script which reads an image and writes a function in MIPS assembly that can draw to a graphical buffer. Used for the CSCB58 Final Project

How to use
#
#
Add an image called c.png in the same directory as the python script.
Run the script 
a file called res.txt is generated and contains the python code. 
before running this block of code, you need to set $t0 to be a graphical buffer
$t1 and $t2 to be the offset of the image, ie the top right corner of where you want to draw the image in the buffer $t0.
