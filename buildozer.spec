[app]

# ── Basic App Info ──────────────────────────────────────────
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example

# ── Source Files ────────────────────────────────────────────
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json,txt

# ── Version ─────────────────────────────────────────────────
version = 0.1

# ── Dependencies ────────────────────────────────────────────
requirements = python3,kivy

# ── Appearance ─────────────────────────────────────────────
orientation = portrait
fullscreen = 0

# ── Android Settings ─────────────────────────────────────────
android.api = 34
android.minapi = 21
android.ndk = 27
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True


# ── Permissions (add what you need) ─────────────────────────
android.accept_sdk_license = True
android.permissions = INTERNET
android.java_memory = 2048
[buildozer]
log_level = 2
