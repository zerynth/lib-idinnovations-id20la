# RFID Reader

# Init serial communication
import streams
streams.serial()

# Import RFID lib
from idinnovations.id20la import id20la


# Function to be called everytime is read
def cb(data):
    # Convert data (bytearray) to ASCII string
    # note: the sensor must be put in ASCII mode (see datasheet).
    id = "".join([chr(c) for c in data])
    print("Read tag:", id)


# Init the reader class, register callback and start reading
reader = id20la.ID20LA(SERIAL2, cb)
print("Ready to read tags!")
