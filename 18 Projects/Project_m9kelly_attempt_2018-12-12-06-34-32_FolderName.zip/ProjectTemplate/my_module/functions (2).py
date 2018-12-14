"""A collection of function for doing my project."""


#This function takes the input of zodiac sign and brings user to a webpage with information about their sign
def main():
    print("The signs are: {}".format(" ".join(SIGNS)))
    sign = ""
    while sign not in SIGNS:
        sign = input("Enter your sign: ").lower().strip()
        if sign == 'capricorn':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/capricorn/')
        elif sign == 'aquarius':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/aquarius/')
        elif sign == 'pisces':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/pisces/')
        elif sign == 'aries':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/aries/')
        elif sign == 'taurus':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/taurus/')
        elif sign == 'gemini':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/gemini/')
        elif sign == 'cancer':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/cancer/')
        elif sign == 'leo':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/leo/')
        elif sign == 'virgo':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/virgo/')
        elif sign == 'libra':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/libra/')
        elif sign == 'scorpio':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/scorpio/')
        elif sign == 'sagittarius':
            webbrowser.open('https://www.astrology-zodiac-signs.com/zodiac-signs/sagittarius/')
        else:
            print("Oops, please check spelling and try again!")
if __name__ == "__main__":
    main()