[app]
# App name and package
title = StoreScannerApp
package.name = StoreScannerApp
package.domain = com.example

# Source files
source.include_exts = py,png,jpg,kv,atlas

# Python version and dependencies
requirements = python3,kivy,plyer

# Android settings
orientation = portrait
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android SDK/NDK versions
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.arch = arm64-v8a,armeabi-v7a

# Allow logging and debug
log_level = 2
warn_on_root = 1
