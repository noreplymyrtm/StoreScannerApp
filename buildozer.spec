[app]
# your app info
title = StoreScannerApp
package.name = StoreScannerApp
package.domain = com.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy,plyer

version = 1.0
orientation = portrait
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# <-- KEY FIX: Pin SDK/NDK versions -->
android.api = 30
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = arm64-v8a,armeabi-v7a
android.build_tools_version = 30.0.3

# Logging
log_level = 2
warn_on_root = 1
