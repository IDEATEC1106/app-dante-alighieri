[app]
title = App Colegio Dante
package.name = appcolegiodante
package.domain = org.colegio
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 1. Agregado cython compatible
requirements = python3,kivy==2.3.0,cython==3.0.8

orientation = portrait
fullscreen = 0

log_level = 2

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk_api = 21

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# ... busca esta línea más abajo en tu archivo .spec y configúrala:
p4a.branch = develop
