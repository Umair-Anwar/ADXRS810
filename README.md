# ADXRS810
This library reads data from gyro adxrs810.

# Dependencies 
You can install PIGPIO library in raspberry pi by following commands
1. wget abyz.co.uk/rpi/pigpio/pigpio.zip
2. unzip pigpio.zip
3. cd PIGPIO
4. make -j4
5. sudo make install
And to start pigpio daemon run 'sudo pigpiod'.

Install bitstream by following command
1. easy_install bitstream

# Usage
gyro.py contain the class ADXRS810 which includes the functions definitions to read data from adxrs810 module.
check.py includes a very simple example to demonstrate the usage of library.
Please take care of minor errors as it is not properly tested.
