from time import sleep
from colorama import Fore, Back


class Battery:
    def __init__(self, mAh, voltage, percent):
        self.V = voltage
        self.capacity = mAh
        self.Wh = self.V * self.capacity * 0.001
        self.percentage = percent
        self.remaining = self.remaining = self.capacity * self.percentage * 0.01

    def is_charging(self, sinking=False):
        return True

    def is_discharging(self, sourcing):
        return True

    def charging(self, input_watt=0.0, input_v=0.0, input_curr=0.0, percent_point=100.0):
        if self.is_charging():
            if percent_point > self.percentage:
                d = percent_point - self.percentage # differential of percentage
            else:
                d = self.percentage - percent_point
            wh = self.Wh * d * 0.01
            print(wh)
            if input_watt == 0.0 and input_v > 0.0 and input_curr > 0.0:
                input_watt = input_curr * input_v
            tt = self.time_taken(wh, input_watt)
            q = input(f"Do you want to charge this battery? [Y]/[N]\nIt will time be taken nearly {tt} hrs.\t:")
            sleep(1)
            if q == "y".casefold():
                m = tt * 60.0
                print(f"Please wait..{m}. seconds")
                print("Charging...")
                # add bms
                sleep(m)
                self.percentage = 100.0
                print(Fore.BLUE, "Charging completed!!!")

    @staticmethod
    def time_taken(wh, power):
        return wh / power

    def percentage(self, mAh):
        return mAh / self.capacity * 100.0

    def __str__(self):
        return str(self.V) + "V" + " " + str(self.capacity)+ "mAh" + "\n " + str(self.Wh) + "Wh"