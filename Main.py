import serial

from barcode_db import get_barcodes_by_name
from barcode_db import close_db
from barcode_db import update_punktezahl


#Programm fuer das Barcode einlesen


def main():
    ser = serial.Serial('COM6', 115200)  # open serial port
    #ser.open()
    print(ser.name)  # check which port was really used
    line = ser.readline().decode()

    while( not(line.find("Ready") >= 0)):
        line = ser.readline().decode()

    bonuspunkte = 0
    print("Barcode einlesen.")

    while(1):
        barcodestring = input()

        if get_barcodes_by_name(barcodestring):
            query_answer = get_barcodes_by_name(barcodestring)

            if (query_answer[0][2] + query_answer[0][3] + query_answer[0][4] + query_answer[0][5] +
                    query_answer[0][6] + query_answer[0][7] + query_answer[0][8]) > 1:
                print(str(query_answer[0][1])+" muss in mehreren Mülltonnen enstorgt werden.")

            if query_answer[0][2] == 1:
                print(str(query_answer[0][1])+" gehört in die gelbe Tonne")
                ser.write(str.encode("0"))
                ser.flush()

                while(1):
                    line = ser.readline().decode()
                    print(line)
                    if (line.find("s") >= 0):
                    #ser.write(str.encode("5"))
                        print("s erhalten")
                        line[0] == ''
                        bonuspunkte = bonuspunkte + int(query_answer[0][9])
                        break
                    if (line.find('t') >= 0):
                    #ser.write(str.encode("6"))
                        print("timeout")
                        line[0] == ''
                        break

            if query_answer[0][3] == 1:
                print(str(query_answer[0][1])+" gehört in die schwarze Tonne")
                ser.write(str.encode("1"))
                ser.flush()

                while(1):
                    line = ser.readline().decode()
                    print(line)
                    if (line.find("s") >= 0):
                    #ser.write(str.encode("5"))
                        print("s erhalten")
                        line[0] == ''
                        bonuspunkte = bonuspunkte + int(query_answer[0][9])
                        break
                    if (line.find('t') >= 0):
                    #ser.write(str.encode("6"))
                        print("timeout")
                        line[0] == ''
                        break

            if query_answer[0][4] == 1:
                print(str(query_answer[0][1])+" gehört in die grüne Tonne")
                ser.write(str.encode("2"))
                ser.flush()

                while(1):
                    line = ser.readline().decode()
                    print(line)
                    if (line.find("s") >= 0):
                    #ser.write(str.encode("5"))
                        print("s erhalten")
                        line[0] == ''
                        bonuspunkte = bonuspunkte + int(query_answer[0][9])
                        break
                    if (line.find('t') >= 0):
                    #ser.write(str.encode("6"))
                        print("timeout")
                        line[0] == ''
                        break

            if query_answer[0][5] == 1:
                print(str(query_answer[0][1])+" gehört in die Bio Tonne")
                ser.write(str.encode("3"))
                ser.flush()

                while(1):
                    line = ser.readline().decode()
                    print(line)
                    if (line.find("s") >= 0):
                    #ser.write(str.encode("5"))
                        print("s erhalten")
                        line[0] == ''
                        bonuspunkte = bonuspunkte + int(query_answer[0][9])
                        break
                    if (line.find('t') >= 0):
                    #ser.write(str.encode("6"))
                        print("timeout")
                        line[0] == ''
                        break

            if query_answer[0][6] == 1:
                print(str(query_answer[0][1])+" gehört in die Braunglas Tonne")
                # passende LED ansteuern
                #für Prototyp irrelevant

            if query_answer[0][7] == 1:
                print(str(query_answer[0][1])+" gehört in die Grünglas Tonne")
                # passende LED ansteuern
                # für Prototyp irrelevant

            if query_answer[0][8] == 1:
                print(str(query_answer[0][1])+" gehört in die Weissglass Tonne")
                # passende LED ansteuern
                # für Prototyp irrelevant

            if query_answer[0][1] == 'User':
                update_punktezahl(query_answer[0][0], bonuspunkte)
                user_punktzahl_update = get_barcodes_by_name(barcodestring)
                print(user_punktzahl_update)
                ser.write(str.encode("7"))
                ser.flush()
                print("Es wurden " + str(bonuspunkte) + " Bonuspunkte gesammelt")
                bonuspunkte = 0
                break

        elif (barcodestring =='Ende'):
            print("Ende")
            break

        else:
            print("Barcode nicht in Datenbank vorhanden")


    close_db()

main()
