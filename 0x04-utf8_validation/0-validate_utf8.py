#!/urs/bin/python3

def validUTF8(data):
    num_bytes_to_check = 0

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte_value = byte & 0xFF

        if num_bytes_to_check == 0:
            # Check how many bytes this character should have
            if byte_value >> 7 == 0:
                num_bytes_to_check = 1
            elif byte_value >> 5 == 0b110:
                num_bytes_to_check = 2
            elif byte_value >> 4 == 0b1110:
                num_bytes_to_check = 3
            elif byte_value >> 3 == 0b11110:
                num_bytes_to_check = 4
            else:
                # Invalid format for the first byte of a character
                return False
        else:
            # Check if the byte starts with the correct continuation bits "10"
            if byte_value >> 6 != 0b10:
                return False

        num_bytes_to_check -= 1

    # If num_bytes_to_check is still positive, it means we are missing some continuation bytes
    return num_bytes_to_check == 0

