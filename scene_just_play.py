import sys
from time import time

import argparse
parser = argparse.ArgumentParser(description='process some integers.')
parser.add_argument('-pn', '--process_num', default='1')
args = parser.parse_args(sys.argv[sys.argv.index("--")+1:])
process_num = int(args.process_num)

from multiprocessing.connection import Listener, Client

IPC_base_port = 6100

IPC_READY_sender = Client(('localhost', IPC_base_port))

import bpy
import blend_render_info

blender_version = bpy.app.version_string

# scene settings, better dont change for shared benchmark
frame_part_born     = 0
subdiv              = 7
scene_frame_end     = 2500001 #  2500001 - 1(init frame) = 2500000 active frames  ~ 3 second benchmark
part_velocity       = 1.0

ps_timestep = 1/1000

srcRadius = 1.0
src_location = [0.0,0.0,0.0]
src_rotation = [0.0,0.0,0.0]
src_scale    = [1.0,1.0,1.0]

### scene
scene = bpy.context.scene
for obj in scene.objects:
    bpy.data.objects.remove(obj, do_unlink=True)
bpy.context.scene.frame_end = scene_frame_end
bpy.types.Scene(bpy.context.scene).use_gravity = False
bpy.types.Scene(bpy.context.scene).gravity = (0, 0, 0)

# print('worker connect', ('localhost', 6001 + process_num))
IPC_START_recv = Listener(('localhost', IPC_base_port + 2 + process_num))

# IPC READY send to coordinator
IPC_READY_sender.send(process_num)

# cpu prewarming ~ 2 sec
a = 1.0
for i in range(30000000):
    a *= 3.1415
    a /= 3.14149

# IPC START waiting from coordinator
msg = IPC_START_recv.accept()

# skip emission and 1st work frame for proper init
bpy.context.scene.frame_set(1)





# play 
time_start = time()

for i in range(2, scene_frame_end + 1):
    bpy.context.scene.frame_set(i)
time_end = time()

# IPC RESULT send to coordinator
IPC_RESULT_sender  = Client(('localhost', IPC_base_port + 1))
IPC_RESULT_sender.send((blender_version, time_start, time_end))

bpy.ops.wm.quit_blender()
