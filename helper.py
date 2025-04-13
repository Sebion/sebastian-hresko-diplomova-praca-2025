def key_to_camelot(key, mode):
    camelot_major = {
        0: "8B", 1: "3B", 2: "10B", 3: "5B", 4: "12B", 5: "7B",
        6: "2B", 7: "9B", 8: "4B", 9: "11B", 10: "6B", 11: "1B"
    }
    camelot_minor = {
        0: "5A", 1: "12A", 2: "7A", 3: "2A", 4: "9A", 5: "4A",
        6: "11A", 7: "6A", 8: "1A", 9: "8A", 10: "3A", 11: "10A"
    }

    if mode == 1:  # Major
        return camelot_major.get(key, "Unknown")
    elif mode == 0:  # Minor
        return camelot_minor.get(key, "Unknown")
    else:
        return "Unknown"


