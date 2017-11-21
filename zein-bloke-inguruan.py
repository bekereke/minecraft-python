from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    behe = mc.getBlock(x,y-1,z)
    #Stevek bi bloke luzeko altuera du
    goi = mc.getBlock(x,y+2,z)
    aurre = mc.getBlock(x+1,y-1,z)
    atze = mc.getBlock(x-1,y-1,z)
    ezker = mc.getBlock(x,y-1,z-1)
    eskuin = mc.getBlock(x,y-1,z+1)
    print("aurre " + str(aurre))
    print("atze " + str(atze))
    print("goi " + str(goi))
    print("behe " + str(behe))
    print("ezker " + str(ezker))
    print("eskuin " + str(eskuin))
    print("-------------")
    sleep(2)