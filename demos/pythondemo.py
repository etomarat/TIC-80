# title:   game title
# author:  game developers, email, etc.
# desc:    short description
# site:    website link
# license: MIT License (change this to your license of choice)
# version: 0.1
# script:  python

last = -1
supported = True

def do_rumble(id):
 global supported
 if id == 0:
  supported = rumble(0, 18000, 0, 80)
 elif id == 1:
  supported = rumble(0, 28000, 0, 120)
 elif id == 2:
  supported = rumble(0, 0, 22000, 80)
 elif id == 3:
  supported = rumble(0, 0, 32000, 120)
 elif id == 4:
  supported = rumble(0, 12000, 45000, 120)
 elif id == 5:
  supported = rumble(0, 42000, 8000, 120)
 elif id == 6:
  supported = rumble(0, 32000, 32000, 160)
 elif id == 7:
  supported = rumble(0, 65535, 65535, 220)

def TIC():
 global last
 cls(1)

 print("GAMEPAD + RUMBLE DEMO", 56, 8, 12)
 print("RT/LT/LB/RB mirror A/B/X/Y", 8, 20, 13)

 if btn(0): print("UP", 8, 36, 11)
 if btn(1): print("DOWN", 8, 46, 11)
 if btn(2): print("LEFT", 8, 56, 11)
 if btn(3): print("RIGHT", 8, 66, 11)
 if btn(4): print("A / SOUTH / RT", 8, 76, 11)
 if btn(5): print("B / EAST / LT", 8, 86, 11)
 if btn(6): print("X / WEST / LB", 8, 96, 11)
 if btn(7): print("Y / NORTH / RB", 8, 106, 11)

 if btnp(0, 20, 4): last = 0; do_rumble(0)
 if btnp(1, 20, 4): last = 1; do_rumble(1)
 if btnp(2, 20, 4): last = 2; do_rumble(2)
 if btnp(3, 20, 4): last = 3; do_rumble(3)
 if btnp(4, 20, 4): last = 4; do_rumble(4)
 if btnp(5, 20, 4): last = 5; do_rumble(5)
 if btnp(6, 20, 4): last = 6; do_rumble(6)
 if btnp(7, 20, 4): last = 7; do_rumble(7)

 print("LAST: " + str(last), 8, 116, 14)
 if not supported:
  print("RUMBLE NOT SUPPORTED", 8, 126, 2)

# <TILES>
# 001:eccccccccc888888caaaaaaaca888888cacccccccacc0ccccacc0ccccacc0ccc
# 002:ccccceee8888cceeaaaa0cee888a0ceeccca0ccc0cca0c0c0cca0c0c0cca0c0c
# 003:eccccccccc888888caaaaaaaca888888cacccccccacccccccacc0ccccacc0ccc
# 004:ccccceee8888cceeaaaa0cee888a0ceeccca0cccccca0c0c0cca0c0c0cca0c0c
# 017:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 018:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# 019:cacccccccaaaaaaacaaacaaacaaaaccccaaaaaaac8888888cc000cccecccccec
# 020:ccca00ccaaaa0ccecaaa0ceeaaaa0ceeaaaa0cee8888ccee000cceeecccceeee
# </TILES>

# <WAVES>
# 000:00000000ffffffff00000000ffffffff
# 001:0123456789abcdeffedcba9876543210
# 002:0123456789abcdef0123456789abcdef
# </WAVES>

# <SFX>
# 000:000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000304000000000
# </SFX>

# <TRACKS>
# 000:100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# </TRACKS>

# <PALETTE>
# 000:1a1c2c5d275db13e53ef7d57ffcd75a7f07038b76425717929366f3b5dc941a6f673eff7f4f4f494b0c2566c86333c57
# </PALETTE>
