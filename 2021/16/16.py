
with open('16.in') as infile:
    input = infile.read()


def hex_to_bin(x):
    bin_str = bin(int(x, 16))
    return bin_str[2:].zfill(len(x) * 4)


def analyze_packet(packet, i):
    start = i

    version = int(packet[i:i + 3], 2)
    type_id = int(packet[i + 3:i + 6], 2)

    i += 6

    if type_id == 4:
        literal = ''

        while True:
            literal += packet[i + 1:i + 5]
            i += 5

            if packet[i - 5] == '0':
                break

        return {
            "version": version,
            "type_id": type_id,
            "literal": int(literal, 2),
            "sub_packets": [],
            "length": i - start,
            "i": i
        }

    else:
        length_type_id = packet[i]
        i += 1

        if length_type_id == '0':
            total_length = int(packet[i:i + 15], 2)
            i += 15
        else:
            total_number = int(packet[i:i + 11], 2)
            i += 11

        sub_packets = []

        while True:
            sub_packet = analyze_packet(packet, i)
            sub_packets.append(sub_packet)

            i = sub_packet["i"]

            if length_type_id == '0':
                total_length -= sub_packet["length"]

                if total_length == 0:
                    break
            else:
                total_number -= 1

                if total_number == 0:
                    break

        return {
            "version": version,
            "type_id": type_id,
            "literal": 0,
            "sub_packets": sub_packets,
            "length": i - start,
            "i": i
        }


def sum_versions(packet):
    sum = packet["version"]

    for sub_packet in packet["sub_packets"]:
        sum += sum_versions(sub_packet)

    return sum


def evaluate_packet(packet):
    type_id = packet["type_id"]

    if type_id == 4:    # literal
        return packet["literal"]

    if type_id == 0:    # sum
        value = 0

        for sub_packet in packet["sub_packets"]:
            value += evaluate_packet(sub_packet)

        return value

    if type_id == 1:    # product
        value = 1

        for sub_packet in packet["sub_packets"]:
            value *= evaluate_packet(sub_packet)

        return value

    if type_id == 2:    # minimum
        value = evaluate_packet(packet["sub_packets"][0])

        for sub_packet in packet["sub_packets"]:
            value = min(value, evaluate_packet(sub_packet))

        return value

    if type_id == 3:    # maximum
        value = evaluate_packet(packet["sub_packets"][0])

        for sub_packet in packet["sub_packets"]:
            value = max(value, evaluate_packet(sub_packet))

        return value

    if type_id == 5:    # greater than
        if evaluate_packet(packet["sub_packets"][0]) > evaluate_packet(packet["sub_packets"][1]):
            return 1

        return 0

    if type_id == 6:    # less than
        if evaluate_packet(packet["sub_packets"][0]) < evaluate_packet(packet["sub_packets"][1]):
            return 1

        return 0

    if type_id == 7:    # equal to
        if evaluate_packet(packet["sub_packets"][0]) == evaluate_packet(packet["sub_packets"][1]):
            return 1

        return 0

    return 0


packets = list(map(hex_to_bin, input.splitlines()))

for packet in packets:
    analyzed_packet = analyze_packet(packet, 0)
    print(evaluate_packet(analyzed_packet))
