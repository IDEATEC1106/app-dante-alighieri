[app]

# (str) Título de tu aplicación
title = Colegio Dante Alighieri

# (str) Nombre del paquete (un solo texto, sin espacios ni caracteres especiales)
package.name = appcolegiodante

# (str) Dominio del paquete (para identificar tu app de forma única en Android)
package.domain = org.colegiodante

# (str) Directorio donde está tu código fuente (el punto actual)
source.dir = .

# (list) Extensiones de archivos que se incluirán en el APK
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

# (list) Archivos a incluir de forma explícita
# source.include_patterns = assets/*,images/*.png

# (str) Versión de tu aplicación
version = 1.0.0

# (list) REQUISITOS IMPORTANTES: Forzamos Python 3.11 para evitar el error de Python 3.14
# ¡Si usas librerías extras (ej. requests), agrégalas al final separadas por comas!
requirements = python3,kivy==2.3.0,cython==0.29.33,pyjnius

# (str) Orientación de la pantalla (landscape, sensorLandscape, portrait o all)
orientation = portrait

# ----------------------------------------------
# Configuraciones específicas de Android
# ----------------------------------------------

# (bool) Indicar si la aplicación es de pantalla completa (True o False)
fullscreen = 1

# (list) Permisos de Android (descomenta si tu app los necesita)
# android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE

# (int) Target Android API (33 o 34 es lo exigido actualmente por Google)
android.api = 34

# (int) API mínima requerida (Android 5.0 en adelante)
android.minapi = 24

# (int) Versión del SDK de Android que se usará
# android.sdk = 33

# (str) Versión del NDK de Android compatible
android.ndk = 26b

# (bool) Aceptar las licencias del SDK de Android automáticamente
android.accept_sdk_license = True

# (str) Arquitecturas de procesador para las que se compilará el APK
android.archs = arm64-v8a

# (str) Forzar el uso de la rama principal de Python para Android
android.p4a_branch = master

# ----------------------------------------------
# Configuración del motor Buildozer
# ----------------------------------------------
[buildozer]

# (int) Nivel de registro (2 muestra toda la información detallada si hay errores)
log_level = 2

# (int) Advertir si se ejecuta como root (en Codespaces es seguro ignorarlo)
warn_on_root = 0
