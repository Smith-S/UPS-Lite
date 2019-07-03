class ups_lite():
    """docstring for ups_lite."""

    def __init__(self):
        """Initialized UPS_Lite setting

        This function set the default setting for UPS-Lite to comunicate with
        RaspberryPi i2c provided by SMBus object.
        ***currently tested on RaspberryPi Zero W***
        """

        # Default i2c device port on RaspberryPi
        # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
        self.bus = smbus.SMBus(1)
        # Low capacity alert on battery
        self.low_capacity = 20

    def battery_status(self):
        """

        This function returns the ramaining capacitiy in int as precentage of
        the battery connected to the UPS-Lite
        """

        # On UPS_Lite, MAX17040G is somehow located at i2c address 0x36
        device_address = 0x36

        # According to MAX17040G datasheet available at
        # https://datasheets.maximintegrated.com/en/ds/MAX17040-MAX17041.pdf
        # the battery’s relative state-of-charge (SOC) is provided at address
        # 04h for MSB
        SOC_MSB = 4
        # 05h for LSB
        SOC_LSB = 5

        def rough_soc(self):
            self.bus.read_byte_data(device_address, SOC_MSB)

        def fine_soc(arg):
            self.bus.read_byte_data(device_address, SOC_LSB)
