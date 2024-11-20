def validUTF8(data):
    """
    Validate if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data set.

    Returns:
        bool: True if data is valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Only consider the last 8 bits of the number
        byte = num & 0xFF

        if num_bytes == 0:
            # Count leading 1s determine the number of bytes the UTF-8 char
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
