#conversion


class Conversion:
    def __init__(self, temp):
        self.temp = int(temp)

    def CtoF(self):
        return self.temp * (9/5) + 32

    def FtoC(self):
        return (self.temp - 32) * (5 / 9)

def menu():
    print ("Temperature Converter")
    print ("1. Celcius to Fahrenheit")
    print ("2. Fahrenheit to Celcius")
    print ("3. Quit\n")
  
def main():
    while True:
        menu()
        user_input = int(input("Select your option: "))
        if user_input == 1:
            temp = float(input("Enter the temperature: "))
            ans = Conversion(temp)
            print (temp, "degree Celcius is {0:.1f} degree Fahrenheit.\n".format(ans.CtoF()))
              
        elif user_input == 2:
            temp = float(input("Enter the temperature: "))
            ans = Conversion(temp)
            print (temp, "degree Fahrenheit is {0:.1f} degree Celcius.\n".format(ans.FtoC()))

        elif user_input == 3:
            break
            
        else:
            print ("Your option is not valid. Please try again.\n")

if __name__ == "__main__":
    main()

    
