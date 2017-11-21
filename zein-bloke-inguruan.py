from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    behe = mc.getBlock(x,y-1,z)
    #Stevek bi bloke luzeko altuera du
    goi = mc.getBlock(x,y+2,z)
    print("goi " + str(goi))
    print("behe " + str(ezker))
    print("-------------")
    sleep(2)
