[app]
title = StoreScannerApp
package.name = storescanner
package.domain = org.example
source.include_exts = py,png,jpg,kv
version = 0.1
orientation = portrait
requirements = python3,kivy,plyer
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android Build settings
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 23b
android.arch = arm64-v8a,armeabi-v7a
