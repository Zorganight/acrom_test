from smd.red import *

SerialPort = "COM3"    # Serial port of the USB gateway module
baudrate = 115200      # Baud rate of the communication
ID_1 = 0                 # ID of the SMD board
ID_2 = 1
master = Master(SerialPort, baudrate)    # Defines the USB gateway module
print(master.scan()) #prints ID list of connected SMDs
master.attach(Red(ID_1))                   # Gives acces to the SMD of specified ID
master.attach(Red(ID_2))

master.set_operation_mode(ID_1, OperationMode.Velocity)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID_1, 100)  #rpm and cpr values are depend on the motor you use.
master.set_shaft_cpr(ID_1, 6533)

master.set_operation_mode(ID_2, OperationMode.Velocity)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID_2, 100)  #rpm and cpr values are depend on the motor you use.
master.set_shaft_cpr(ID_2, 6533)

master.pid_tuner(ID_1)                 # Starts the PID auto-tune process
time.sleep(30)    # Waits 30 seconds for the process to complete
master.pid_tuner(ID_2)                 # Starts the PID auto-tune process
time.sleep(30)

print(master.get_control_parameters_velocity(ID_1))    # Prints the calculated PID values
print(master.get_control_parameters_velocity(ID_2))    # Prints the calculated PID values
time.sleep(5)


master.enable_torque(ID_1, True)      #enables the motor torque to start rotating
master.enable_torque(ID_2, True)      #enables the motor torque to start rotating

master.set_velocity(ID_1, 50)          # Sets motor to operate at 50 RPM
master.set_velocity(ID_2, 50)          # Sets motor to operate at 50 RPM