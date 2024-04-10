#!/bin/bash

# Verificar si se proporciona un archivo como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <archivo>"
    exit 1
fi

archivo=$1

# Verificar si el archivo existe
if [ ! -f "$archivo" ]; then
    echo "El archivo $archivo no existe."
    exit 1
fi

# Dar permisos de ejecución al archivo
chmod +x "$archivo"

# Cambiar la propiedad del archivo a root
sudo chown root "$archivo"

echo "Se han cambiado los permisos del archivo $archivo y ahora es propiedad de root."
