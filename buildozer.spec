[app]
title = App Colegio Dante
package.name = appcolegiodante
package.domain = org.colegio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 1. Requerimientos con Cython e instrucciones de renderizado estables
requirements = python3,kivy==2.3.0,cython==0.29.37

orientation = portrait
fullscreen = 0

# 2. Forzar visualización de errores detallados en la consola de GitHub
log_level = 2

# 3. Configuración estricta de APIs y fijación del NDK compatible (r25b)
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.ndk = 25b

# 4. Arquitecturas objetivo para la Google Play Store (64 y 32 bits)
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# 5. Rama de desarrollo de python-for-android para compatibilidad moderna
p4a.branch = develop
