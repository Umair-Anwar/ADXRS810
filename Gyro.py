"""
This Library reads data from gyro adxrs810.
"""
import pigpio 
import time
from bitstring import BitStream

class ADXRS810:

    def __init__(self):

        #commands to read data from adxrs180
        self.Sensor_data_CHK_asr =    [1,0,0,3]  #0x20000003 #
        self.Sensor_data_CHK_de_asr = [32,0,0,0] #0x20000000 #
        self.Read_Rate =   [128,0,0,0]           #0x80000000 #
        self.Read_Tem =    [128,4,0,1]           #0x80040001 #
        self.Read_Locst =  [128,8,0,1]           #0x80080001 #
        self.Read_Hicst =  [128,12,0,0]          #0x800C0000 #
        self.Read_Quad =   [128,16,0,1]          #0x80100001 #
        self.Read_Fault =  [128,20,0,0]          #0x80140000 #
        self.Read_Pid =    [128,24,0,0]          #0x80180000 #
        self.Read_SN3_2 =  [128,28,0,1]          #0x801C0001 #
        self.Read_SN1_0 =  [128,32,0,1]          #0x80200001 #
        
        self.spi1 =pigpio.pi()
        self.h = self.spi1.spi_open(0,20000000,20000)
        
        # add start up sequence according to datasheet
        print ('Initialising ADXRS180')
        time.sleep(0.1)
        (count,first_data) = self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_asr)
        time.sleep(0.05)
        self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_de_asr)            # ignor responce data this time 
        time.sleep(0.05)
        (count,st)=self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_de_asr) # check status bits, should be 0b10
        (count,st)=self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_de_asr) # status bits 0b10 and ready to use otherwise error
        print ('status ok and ready to use')
    # We send two read command to read a register data, bcz data latching in adxrs180  
    
    def Sensor_Data(self):
        self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_de_asrRead_Rate)
        (count,st)=self.spi1.spi_xfer(self.h,self.Sensor_data_CHK_de_asrRead_Rate)
        f2 = BitStream(bytes = st )
        f2.pos= 6
        a=f2.read(16).int
        return a

        
    def Rate(self):
        self.spi1.spi_xfer(self.h,self.Read_Rate)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Rate)
        f2 = BitStream(bytes = st )
        f2.pos= 11
        a=f2.read(16).int
        a=a/80
        return a
    
    def Tem(self):
        self.spi1.spi_xfer(self.h,self.Read_Tem)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Tem)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a

    def Locst(self):
        self.spi1.spi_xfer(self.h,self.Read_Locst)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Locst)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    def Hicst(self):
        self.spi1.spi_xfer(self.h,self.Read_Hicst)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Hicst)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    
    def Quad(self):
        self.spi1.spi_xfer(self.h,self.Read_Quad)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Quad)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    
    def Fault(self):
        self.spi1.spi_xfer(self.h,self.Read_Fault)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Fault)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    
    def Pid(self):
        self.spi1.spi_xfer(self.h,self.Read_Pid)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_Pid)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    
    def SN3_2(self):
        self.spi1.spi_xfer(self.h,self.Read_SN3_2)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_SN3_2)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a
    
    def SN1_0(self):
        self.spi1.spi_xfer(self.h,self.Read_SN1_0)
        (count,st)=self.spi1.spi_xfer(self.h,self.Read_SN1_0)
        f2 = BitStream(bytes = st)
        f2.pos= 11
        a=f2.read(16).bin
        return a






