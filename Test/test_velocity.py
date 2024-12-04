from smd.red import *

SerialPort = "COM3"    # Serial port of the USB gateway module
baudrate = 115200      # Baud rate of the communication
ID = 0                 # ID of the SMD board

master = Master(SerialPort, baudrate)    # Defines the USB gateway module
print(master.scan()) #prints ID list of connected SMDs
master.attach(Red(ID))                   # Gives acces to the SMD of specified ID

master.set_operation_mode(ID, OperationMode.Velocity)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID, 100)        # Defines the motor RPM value as 100
master.set_shaft_cpr(ID, 6533)       # Defines the motor CPR value as 6533
master.pid_tuner(ID)                 # Starts the PID auto-tune process
time.sleep(30)    # Waits 30 seconds for the process to complete
print(master.get_control_parameters_velocity(ID))    # Prints the calculated PID values

master.enable_torque(ID, True)       # Enables motor to operate
master.set_velocity(ID, 50)          # Sets motor to operate at 50 RPM