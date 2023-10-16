from battery import Battery




class PowerBank(Battery):
    def __init__(self, mAh, v=3.7, percent=100):
        super().__init__(mAh, v, percent)

    class Meta:
        modal = Battery


class Phone(Battery):
    def __init__(self, mAh=5000, v=3.7, percent=100):
        super().__init__(mAh, v, percent)

class Device:
    def __init__(self, mAh, volt=3.7):
        self.capacity = mAh
        self.voltage = volt
        self.percent = 0.0
        self.Wh = self.voltage * self.capacity * 0.001

    def checkout(self, power_source):
        if self.capacity < power_source.capacity:
            return False
        else:
            return True

    def charging(self, power_source, sinking=False, is_fast_charge=False):
        if sinking:
            print(power_source.capacity)

            capacity = power_source.capacity - (self.capacity - (self.capacity * 0.01 * self.percent))
            percent = power_source.percent(capacity)
            power_source.capacity = capacity
            return format(percent, '.0f')
        else:
            return PermissionError("You are not permit to charge.")



class Battery:
    def __init__(self, capacity, voltage):
        self.capacity = capacity
        self.healthy = None
        self.voltage = voltage
        self.Wh = self.voltage * self.capacity * 0.001

    def is_charging(self, power_source=0):

        if power_source == 0:
            return False
        elif power_source > 1:
            return True
        else:
            self.is_discharge(1)

    def is_discharge(self, status):
        if status == 1:
            return True
        else:
            return False

    def charging_time(self, input_watt=0.0, input_volt=0.0, input_current=0.0, current_percent=0.0, full_percent=100.0):
        if self.is_charging():
            deta = full_percent - current_percent
            wh = self.Wh * deta * 0.01
            if input_watt > 0.0:
                return wh / input_watt
            elif input_current > 0.0 and input_volt:
                return self.Wh / (input_current * input_volt)
            else:
                if input_current == 0.0 or input_volt == 0.0:
                    raise ValueError("You can't charge. Some issue was happened.")
                else:
                    raise ValueError("Wrong value will no work")

    def discharge_time(self, *loads):
        """

        :param loads: the list of loads
        :return: time taken
        """
        total = 0.0
        for l in loads:
            total += l
        time = self.Wh / total
        return time

    def deta_capacity(self, p1, p2):

        '''
        :param p1: bt_percent for current
        :param p2: bt_percent for second point
        :return: Capacity
        '''

        if p1 < p2:
            deta = p2 - p1
        else:
            deta = p1 - p2
        if p1 <= 1 or p2 <= 1:
            return self.capacity * deta
        else:
            return self.capacity * deta * 0.01

    def current_capacity(self, percent):
        return percent * self.capacity * 0.01

    def it_will_remain_percent(self,battery_percent, device_mAh=0.0, device_percent=0.0, ):

        if device_mAh > 0:
            device_mAh = device_mAh - (device_percent * 0.01 * device_mAh)
            return (
                    self.percent(self.current_capacity(percent=battery_percent) - device_mAh)
            )

    def percent(self, mAh):
        return mAh / self.capacity * 100

    def __str__(self):
        return str(self.voltage) + "V" + " " + str(self.capacity)+ "mAh" + "\n " +str(self.Wh) + "Wh"

def hr_min(hrs):
    if hrs > 1:
        hr = int(hrs % 60)
        mins = int((hrs - hr) * 60)
        return f"{hr} hr, {mins} minutes"
    else:
        return f"{format(hrs * 60, '.0f')} mins"


if __name__ == '__main__':
    kanote = PowerBank(39900, 3.7, percent=33)
    print(kanote.Wh)
    print(kanote.get_capacity())
    kanote.charging(65, percent_point=93)
    print(kanote.get_capacity())
