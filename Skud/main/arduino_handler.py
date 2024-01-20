import serial
import serial.tools.list_ports
from .models import *


ports = list(serial.tools.list_ports.comports())
for port in ports:
    if "Arduino" in port.description:
        device = port.device
arduino = serial.Serial(device, 9600)

# key_id = 25763
# clef_id = 4294940973


def arduino_reader():
    teacher_key = ''
    office_key = ''
    while teacher_key == '' or office_key == '':
        data = arduino.readline()
        line = "".join(c for c in str(data) if c.isnumeric())
        current_office = Office.objects.filter(card_number=line)
        current_teacher = Teacher.objects.filter(card_number=line)
        if current_office:
            office_key = current_office
        elif current_teacher:
            teacher_key = current_teacher
    try:
        return office_key, teacher_key
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    pass
