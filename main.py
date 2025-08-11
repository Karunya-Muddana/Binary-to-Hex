radix = 2
inp = input("Give your binary number --> ")

#I padded with 0s for smooth operation
while len(inp) % 4 != 0:
    inp = '0' + inp

hex_digits = []

# Process 4 bits at a time
for i in range(0, len(inp), 4):
    chunk = inp[i:i+4]
    decimal_value = int(chunk, radix)  # New knowledge you can simply convert binary to desimal by giving base
    hex_digit = hex(decimal_value)  # the hex operator makes any decimal value into hex but with 0x so we remove it by only takin last 2 elements and turning them upper
    hex_digit = hex_digit[2:]
    hex_digit.upper
    hex_digits.append(hex_digit)

hex_string = ''.join(hex_digits)
print(f"Hexadecimal: {hex_string}")
