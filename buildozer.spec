[app]
# (str) Title of your application
title = AI Quantitative Analytics

# (str) Package name
package.name = scamsimulator

# (str) Package domain (needed for android packaging)
package.domain = org.scam

# (list) Source files to include (let it include all python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

#
# Android specific
#
fullscreen = 0
android.permissions = INTERNET
