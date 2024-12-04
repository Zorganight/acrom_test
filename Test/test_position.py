from smd.red import *

MASTER_PORT =  "COM10"
master = Master(MASTER_PORT) #creating master object
print(master.scan())
ID = 0 

master.set_operation_mode(ID, OperationMode.Position)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID, 100)  #rpm and cpr values are depend on the motor you use.
master.set_shaft_cpr(ID, 6533)
master.pid_tuner(ID)                 # Starts the PID auto-tune process
time.sleep(30)    # Waits 30 seconds for the process to complete
print(master.get_control_parameters_velocity(ID))    # Prints the calculated PID values
time.sleep(5)

master.enable_torque(ID, True)      #enables the motor torque to start rotating

while True:
    master.set_position(ID, 5000)   #sets the setpoint to 5000 encoder ticks.
    time.sleep(1.2)
    master.set_position(ID, 0)      #sets the setpoint to 0 encoder ticks. Motor goes to start
    time.sleep(1.2)
