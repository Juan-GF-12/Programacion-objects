import bcrypt

# Hashear una contraseña antes de almacenarla
def hash_contraseña(contraseña):
    return bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())

# Validar una contraseña al inicio de sesión
def validar_contraseña(contraseña, hash_guardado):
    return bcrypt.checkpw(contraseña.encode(), hash_guardado)
