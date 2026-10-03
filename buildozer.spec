[app]
title = appcolegiodante
package.name = appcolegiodante
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy==2.3.0, cython==0.29.37, pyjnius
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.bootstrap = sdl2
