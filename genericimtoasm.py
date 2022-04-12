
# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"c.png")
px = im.load()
w, h = im.size


for i in range(w):
    for j in range(h):
        print(px[i, j])

register_temp = "$t6"
opcode = "sw "


f = open("res.txt", "w")

jump_init = "\tmove $t3, $zero\n"
f.write(jump_init)
rgb_prev = "prev"
def color_normal_form(r,g,b): #if r = B in hex then make it r = 0b
    #If the hex converted is a single digit, then append a 0 to the front to follow the RR,GG,BB form
    
    #
    r.strip()
    g.strip()
    b.strip()

    
    if(len(r) == 1):
        r = "0" + r

    if(len(g) == 1):
        g = "0" + g
    
    if(len(b) == 1):
        b = "0" + b

    return "0x" + r+g+b



for i in range(h): #y 
    for j in range(w): #x
        print(px[j, i])
        #Instruction to load color
        #Instruction to write to output buffer.
        #Generate color
        if(px[j, i] == (255, 255, 255, 255)): #If white background.
            location_asm = "\taddi $t2, $t2, 4\n"
            f.write(location_asm)
            continue
        #loop continue => not white. 
        
        #Write color instruction
        rgb = color_normal_form(str(hex(px[j, i][0]))[2:], str(hex(px[j, i][1]))[2:], str(hex(px[j, i][2]))[2:]) 
        
        opcode_w = "\tli " +  register_temp + "," + rgb + "\n" #store color pixel. 
        if(rgb_prev != opcode_w):
            f.write(opcode_w)
            rgb_prev = opcode_w
            
            
        
        #Write Buffer instruction:
        final_address_asm = "\tadd $t4, $t2, $t0\n"
        f.write(final_address_asm)
        
        
        opcode_buffer = "\t"+ opcode + register_temp + ", " + "($t4)" + "\n"
        
        f.write(opcode_buffer)

        location_asm = "\taddi $t2, $t2, 4\n"
        f.write(location_asm)        
        

    location_jump_asm = "\taddi $t3, $t3, 256\n"
    f.write(location_jump_asm)        
        

    location_jump_asm = "\tadd $t2, $t1, $t3\n"
    f.write(location_jump_asm)    

        
    
f.close()
