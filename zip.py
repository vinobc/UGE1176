first_names = ["Steve", "Mohindar", "Kishore"]
last_names = ["Kumar", "Amarnath", "Smith"]
print([' '.join(n) for n in zip(first_names, last_names[::-1])])
