import serialmodule as sm

def main():
    SerialModule = sm.SerialPortControl()
    device = SerialModule.getPort()
    SerialModule.serialObjectCreate(device)


if __name__ == '__main__':
    main()
