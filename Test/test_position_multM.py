from smd.red import *

MASTER_PORT =  "COM10"
master = Master(MASTER_PORT) #creating master object
print(master.scan())
ID_1 = 0
ID_2= 1

master.set_operation_mode(ID_1, OperationMode.Position)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID_1, 100)  #rpm and cpr values are depend on the motor you use.
master.set_shaft_cpr(ID_1, 6533)

master.set_operation_mode(ID_2, OperationMode.Position)    # Sets the motor's operation mode as "Velocity"
master.set_shaft_rpm(ID_2, 100)  #rpm and cpr values are depend on the motor you use.
master.set_shaft_cpr(ID_2, 6533)

master.pid_tuner(ID_1)                 # Starts the PID auto-tune process
time.sleep(30)    # Waits 30 seconds for the process to complete
master.pid_tuner(ID_2)                 # Starts the PID auto-tune process
time.sleep(30)

print(master.get_control_parameters_position(ID_1))    # Prints the calculated PID values
print(master.get_control_parameters_position(ID_2))    # Prints the calculated PID values
time.sleep(5)


master.enable_torque(ID_1, True)      #enables the motor torque to start rotating
master.enable_torque(ID_2, True)      #enables the motor torque to start rotating


try:
    while True:
        degree = int(input("Enter the degree (integer value): "))
        M_count_1 = degree / 6533
        M_count_2 = degree / 6533

        master.set_position(ID_1, M_count_1)
        master.set_position(ID_2, M_count_2)
        time.sleep(1.2)

except KeyboardInterrupt:
    print("Exiting program...")
    master.enable_torque(ID_1, False)
    master.enable_torque(ID_2, False)


