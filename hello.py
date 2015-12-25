from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Hello World Inyoo")
x, y, z = mc.player.getPos()
mc.postToChat("my location is %f %f %f"  % (x, y, z,))       
x,y,z=mc.player.getPos()
mc.player.setPos(0, 0, 0)