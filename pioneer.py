import sim
import sys

class Pioneer:

    def __init__(self):
        sim.simxFinish(-1) # Ends any existing communication threads
        self.clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
        if self.clientID != -1:
            print("Connected to remote API server")
        else:
            print("Connection unsuccessful :(")
        errorCode, self.left_motor_handle = sim.simxGetObjectHandle(self.clientID, "Pioneer_p3dx_leftMotor", sim.simx_opmode_oneshot_wait)
        errorCode, self.right_motor_handle = sim.simxGetObjectHandle(self.clientID, "Pioneer_p3dx_rightMotor", sim.simx_opmode_oneshot_wait)


    def move_pioneer(self,left_speed,right_speed):
        sim.simxSetJointTargetVelocity(self.clientID, self.left_motor_handle, left_speed, sim.simx_opmode_streaming)
        sim.simxSetJointTargetVelocity(self.clientID, self.right_motor_handle, right_speed, sim.simx_opmode_streaming)    
