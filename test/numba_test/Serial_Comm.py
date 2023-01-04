import serial
import time
from numba import jit
resolution = 0.1

'''
# t(ID)(DLC)(DATA)<CR>
t123 5 61 62 63 64 65<CR>  ID=0x123, Data Length=5, Data1=0x61, Data2=0x62,
Data3=0x63, Data4=0x64, Data5=0x65인 CAN Frame을 전송
'''
@jit(nopython=True, cache=True)
def Preoperation_Set():
    return 't00028000\r' 
@jit(nopython=True, cache=True)
def Operation_Set():
    return 't00020100\r' 
@jit(nopython=True, cache=True)
def Sync():
    return 't08000000\r'
@jit(nopython=True, cache=True)
def Node_ID_Read():
    return 't00080000000000000000\r'

ser = serial.Serial("COM6", 115200, timeout=1)  # COM 6에 115200으로 serial port open
op = Preoperation_Set()
ser.write(op.encode())
op = Operation_Set()
ser.write(op.encode())

@jit(nopython=True, cache=True)
def Serial_Comm(resolution,ser,op):
    while True:
        start = time.time()
        ser.write(Sync().encode()) # Sync 데이터 전송
        rx = ser.readline() # 아스키 타입으로 읽음
        RAW = str(rx).split('t')
        #print('RAW = ',rx)
        if len(RAW) > 1:
            temp1 = RAW[1]
            x = ''+temp1[6:8]+temp1[4:6]
            print(temp1[6:8],',',temp1[4:6],',X = ',x,',RAW = ',temp1)
            y = ''+temp1[10:12]+temp1[8:10]
            print(temp1[10:12],',',temp1[8:10],',y = ',y,',RAW = ',temp1)      
            x1 = (int(x, 16)*resolution) 
            y1 = (int(y, 16)*resolution)
            print('x = ',x1)
            print('y = ',y1)
            end = time.time()
            result = end - start
        print("Time elapsed: ", result)  # seconds
    ser.close()   # serial 통신 close
#if __name__ == "__main__":
Serial_Comm(resolution,ser,op)