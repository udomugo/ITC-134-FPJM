import sys

from conversion import Conversion

def test(did_pass):
    ''' Print the result of a test. '''
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = ('Test at line {0} FAILED.'.format(linenum))
    print(msg)
#test(menu() == print('BOB Blob Temperatur Converter\n1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\n3. Quit\n'))
test(Conversion.CtoF(Conversion(0))==32)
test(Conversion.FtoC(Conversion(32))==0)
test(Conversion.CtoF(Conversion(-40))==-40)
