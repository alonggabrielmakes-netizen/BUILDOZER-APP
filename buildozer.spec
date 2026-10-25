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
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accepts_license = True

# ── Permissions (add what you need) ─────────────────────────
android.permissions = INTERNET

[buildozer]
log_level = 2
