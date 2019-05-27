.. module:: id20la

*************
ID20LA Module
*************

    .. _datasheet: http://id-innovations.com/httpdocs/ID-serise%20HID-EM2013-6-7.pdf

    This module contains the Zerynth driver for ID-20LA RFID tag reader from ID
    Innovation. This is the ID-20LA, a very simple to use RFID reader module from
    ID Innovations. With a built in antenna, the only holdup is the 2mm pin spacing
    (breakout board available below). Power the module, hold up a 125kHz card, and
    get a serial string output containing the unique ID of the card.
.. class:: ID20LA(serial_port, callback, read_timeout=100)

    Creates in instance of the ID20LA class.

    :param serial_port: Serial port to be used (RX only). (i.e. SERIAL2)
    :param callback: Callback to be called whenever a tag is read.
    :param read_timeout: Milliseconds to wait when polling sensor. (Default: 100)

    The serial communication is initialized using the specified serial port.
    The TX pin is not used since the communication is one-way only.

    The callback must take exactly one argument, which will be the 10-bytes
    bytearray read from the tag. It is suggested to put the ID-20LA in ASCII
    mode to be able to decode the 10 bytes as 10 characters, refer to datasheet
    for further informations.

    
.. method:: stop()

        This method stops the reading from the sensor.

        
