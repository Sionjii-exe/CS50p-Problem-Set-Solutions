# E = MC^2
# Prompts the user for mass in integer (kilograms)
mass = int(input("Enter the mass in kilograms: "))

# Calculates the energy in joules using the formula E = mc^2, where c is the speed of light (approximately 3 x 10^8 m/s).
c = 3 * (10 ** 8)  # speed of light in m/s
energy = mass * (c ** 2)  # Calculate energy using E = mc^2
print(energy)  # Output the energy in joules
