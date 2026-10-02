[app]
title = App Colegio Dante
package.name = appcolegiodante
package.domain = org.colegio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

# Dejamos que Buildozer use sus propias rutas limpias automáticamente
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk_api = 21

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
