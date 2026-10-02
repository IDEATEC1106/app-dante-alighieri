[app]
# Nombre y paquete de la aplicación
title = App Colegio Dante
package.name = appcolegiodante
package.domain = org.colegio

# Archivos a incluir
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requisitos y librerías de Python
requirements = python3,kivy==2.3.0

# Configuración de pantalla
orientation = portrait
fullscreen = 0

# Configuración de Rutas del SDK de Android para GitHub Actions
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk-bundle
android.accept_sdk_license = True

# Versiones estables de la API de Android
android.api = 34
android.minapi = 21
android.ndk_api = 21
android.bootloader_api = 34

# Arquitecturas admitidas y permisos básicos
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
