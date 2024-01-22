import serial
import serial.tools.list_ports
from .models import *


ports = list(serial.tools.list_ports.comports())
for port in ports:
    if "Arduino" in port.description:
        device = port.device
try:
    arduino = serial.Serial(device, 9600)
except Exception as ex:
    arduino = None

# key_id = 25763
# clef_id = 4294940973


def arduino_reader():
    logged_teacher_card = ''
    logged_office_card = ''
    while logged_teacher_card == '' or logged_office_card == '':
        data = arduino.readline()
        line = "".join(c for c in str(data) if c.isnumeric())
        current_office = Office.objects.filter(card_number=line)
        current_teacher = Teacher.objects.filter(card_number=line)
        if current_office:
            logged_office_card = line
        elif current_teacher:
            logged_teacher_card = line
    try:
        return logged_office_card, logged_teacher_card
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    pass
