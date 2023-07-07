import PySimpleGUI as sg
from com import *
import webbrowser

url = 'https://github.com/Matp101/Car-Cluster-Cloner'

sg.theme('DarkAmber')   # Add a touch of color

data = 'AAAA AFEF EE40 0A28  2833 FFFF FFFF 0326  0312 20CB FFFF FFFF  FFFF FFFF FFFF 9B00\n21AF ADC2 0006 3183  07D0 2EE0 55F0 63EE  0BCE 01BD 0A1A 1277  1575 C956 97BF 0393\n9482 0000 1351 03E8  0FA0 1D4C 2031 E0FB  01D8 077B 0E12 0F77  153E 30C0 0C18 FFFF\nFFFF 001B 97FF FFFF  FF00 FF0B 819C 1C50  1E36 0C05 0509 019E  2804 0205 1402 0AFF\n2637 333F FFFF FFFF  FFFF 00F3 2009 2C2C  0CFF FFFF 0D25 FF90  FF00 FF00 FFFF 0090\n0000 0000 FFFF FFFF  00FF FFFF FFFF FFFF  FFFF FFFF 57FF FF2D  00FF 0000 017A 5AFF\n7DFF 94FF A0FF 10EC  0094 047D 047D 0827  5644 555A A097 99FF  FFFF 08A1 FFFF FFFF\nFFFF FFFF FFFF FFFF  FFFF FFFF 05FF 0005  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\n0000 0000 0000 0000  00FF 0000 0000 0000  0000 00FF 0000 0000  0000 0000 00FF 0000\n0000 0000 0000 00FF  0000 0000 FFFF FFFF  00FF 3CFF 0807 0605  0404 CC30 0301 0001\n0000 0000 0AFC FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\nFFFF FFFF 5FFF 3894  FFFF FFFF 0CF3 FD62  FD70 FFFF FFFF 0FED  FFFF FF0A FFEA FFFF\n201F FFFF 5A5A 5A5A  FFFF 00FF FFFF FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\n33D0 CC2F 33D0 CC2F  33D0 CC31 33CE CC31  33CE CC31 33CE CC31  33CE CC31 33CE CC31\n02FD E300 007C E283  0226 E3DB 0267 E39A  0285 E378 02A2 E35F  02D2 E12F 06AF E056\n010D 03F3 04F1 030A  58F9 29A6 05D1 4410  E17D 0237 0005 0206  FFFF 0000 0000 0000\nAAAA AFEF EE40 0A28  2833 FFFF FFFF 0326  0312 20CB FFFF FFFF  FFFF FFFF FFFF 9B00\n21AF ADC2 0006 3183  07D0 2EE0 55F0 63EE  0BCE 01BD 0A1A 1277  1575 C956 97BF 0393\n9482 0000 1351 03E8  0FA0 1D4C 2031 E0FB  01D8 077B 0E12 0F77  153E 30C0 0C18 FFFF\nFFFF 001B 97FF FFFF  FF00 FF0B 819C 1C50  1E36 0C05 0509 019E  2804 0205 1402 0AFF\n2637 333F FFFF FFFF  FFFF 00F3 2009 2C2C  0CFF FFFF 0D25 FF90  FF00 FF00 FFFF 0090\n0000 0000 FFFF FFFF  00FF FFFF FFFF FFFF  FFFF FFFF 57FF FF2D  00FF 0000 017A 5AFF\n7DFF 94FF A0FF 10EC  0094 047D 047D 0827  5644 555A A097 99FF  FFFF 08A1 FFFF FFFF\nFFFF FFFF FFFF FFFF  FFFF FFFF 05FF 0005  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\n0000 0000 0000 0000  00FF 0000 0000 0000  0000 00FF 0000 0000  0000 0000 00FF 0000\n0000 0000 0000 00FF  0000 0000 FFFF FFFF  00FF 3CFF 0807 0605  0404 CC30 0301 0001\n0000 0000 0AFC FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\nFFFF FFFF 5FFF 3894  FFFF FFFF 0CF3 FD62  FD70 FFFF FFFF 0FED  FFFF FF0A FFEA FFFF\n201F FFFF 5A5A 5A5A  FFFF 00FF FFFF FFFF  FFFF FFFF FFFF FFFF  FFFF FFFF FFFF FFFF\n33D0 CC2F 33D0 CC2F  33D0 CC31 33CE CC31  33CE CC31 33CE CC31  33CE CC31 33CE CC31\n02FD E300 007C E283  0226 E3DB 0267 E39A  0285 E378 02A2 E35F  02D2 E12F 06AF E056\n010D 03F3 04F1 030A  58F9 29A6 05D1 4410  E17D 0237 0005 0206  FFFF 0000 0000 0000\n'

main_layout = sg.Frame('',[
                        [sg.Text('Welcome to the Car Cluster Cloner!')],
                        [sg.Text('Made by: Matp101')],
                        [sg.Text(url, enable_events=True, key='link')],
                        ], element_justification='center', size=(300, 100))

com_layout = sg.Frame('COM Port',[
                      [sg.Text('Please Select A COM Port', justification='center')],
                      [sg.Combo(values=(''), default_value='', readonly=False, k='comselect', enable_events=True, size=(10,1))],
                      [sg.Button('Connect', enable_events=True, key='connect'),
                      sg.Button('Disconnect', enable_events=True, key='disconnect')],
                        [sg.Text('Disconnected', key='status', justification='center')],
                      ], element_justification='center', size=(300, 140))

readscr_layout = sg.Frame('Transfer',[
                        [sg.Button('Read Source', size=(15,1))],
                        [sg.Button('Read Destination', size=(15,1))],
                        [sg.Button('Clone', size=(15,1))]
                        ], element_justification='center', size=(300, 125))

text_layout = sg.Frame('Output',[
    [sg.Multiline(data,
        #'Output Data',
        #'Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.', 
                
                font=('Courier', 10), justification='center', size=(45,5), expand_x=True, expand_y=True, k='databox')],
    [sg.Button('Save', size=(15,1))]]
                 , element_justification='center', size=(720, 320))



left_side = sg.Column([[main_layout], [com_layout], [readscr_layout]])

right_side = sg.Column([[text_layout]])



layout=[[left_side, right_side]]


    
# Create the window
window=sg.Window('Car Cluster Cloner', layout, finalize=True)      # Part 3 - Window Defintion
#window = sg.Window('Example Window', text_layout, finalize=True)
comports = get_available_com_ports()
window['comselect'].update(values=comports)


# Display and interact with the Window
# Part 4 - Event loop or Window.read call
while True:
    event, values = window.read()
    ard = arduino()
    if event == sg.WINDOW_CLOSED:
        ard.disconnect_arduino()
        break
    elif event == 'link':
        webbrowser.open(url)
    elif event == 'connect':
        com = values['comselect']
        print(com)
        if com != '':
            print('Connecting to ' + com)
            ard.connect_arduino(com)
            if ard.get_status():
                window['status'].update('Connected')
            else:
                window['status'].update('Failed to Connect')
    elif event == 'disconnect':
        ard.disconnect_arduino()
        window['status'].update('Disconnected')
    elif event == 'Read Source':
        ard.send_data_to_arduino('1')
        data = ard.read_data()
        window['databox'].update(data)
    elif event == 'Read Destination':
        ard.send_data_to_arduino('2')
        data = ard.read_data()
        window['databox'].update(data)
    elif event == 'Clone':
        ard.send_data_to_arduino('3')
        data = ard.read_data()
        window['databox'].update(data)
    

window.close()                                  # Part 5 - Close the Window
exit(0)