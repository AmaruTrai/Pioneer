import vrep
import time
import math

print ('Program started')
startTime = time.time()
vrep.simxFinish(-1)
clientID = vrep.simxStart('127.0.0.1',19999,True,True,-500000,5)

if clientID != -1:
    print('Connection estabilished')
    
    x = 0
    y = 0
    z = 0.1
    realTime = 0
    res, target = vrep.simxGetObjectHandle(clientID, 'Sphere',vrep.simx_opmode_oneshot_wait)
    
    while (realTime) < 60000 :
       #time.sleep(0.1)
       realTime = time.time() - startTime
       theta = realTime/10
       x = math.sin(theta*2)
       y = 2*math.cos(theta)
       #x = x + 0.00001
       #y = y + 0.00001
       XYZ = [x, y, z]
       vrep.simxSetObjectPosition(clientID, target, -1, XYZ, vrep.simx_opmode_oneshot)
       print(theta)
    
    vrep.simxGetPingTime(clientID)
    vrep.simxFinish(clientID)
else:
    print('No Connection')
print('End of programm')

