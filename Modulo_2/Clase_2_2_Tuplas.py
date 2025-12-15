# --- TUPLAS: LA SEGURIDAD ANTE TODO ---

# Definimos una configuración inmutable (Como un Preset de Fábrica)
configuracion_audio = ("44.1kHz", "16 bit", "Stereo")

print("Configuración actual:", configuracion_audio)
print("Frecuencia de muestreo:", configuracion_audio[0])

# INTENTO DE SABOTAJE (Descomenta la linea de abajo para ver el error)
# configuracion_audio[0] = "48kHz"

# Al ejecutar la línea de arriba, Python gritará:
# TypeError: 'tuple' object does not support item assignment
