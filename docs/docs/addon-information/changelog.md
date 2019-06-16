---
layout: default
title: Changelog
parent: Addon Information
nav_order: 2
---
# Changelog
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Version 0.1.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.1.0/rizomuv_bridge.zip)

### Improved
- Improved string concatenation during lua script construction.

### Known Bugs

- [Does not work in local view](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/2).
- Texture map not loading.

---

## Version 0.2.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.2.0/rizomuv_bridge.zip)

### Improved
- Improved error catching and added report messages.

### Fixed
- Fixed [local view bug](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/2)
- Fixed Texture Map loading

### Added
- Added support for multiple UV sets.
- Added links to documentation in addon preferences.

---

## Version 0.2.1
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.2.1/rizomuv_bridge.zip)

### Changed
- Changed startup script default to Sharp Edges Unwrap.

### Added
- Added option to automatically create seams and sharp edges from UV island boundaries.


## Version 0.3.0
{: .d-inline-block }
STABLE
{: .label .label-green }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.3.0/rizomuv_bridge.zip)

### Improved
- Reorganised UI into more distinct sections so it is easier for me to expand in the future.
- More action reports.


### Changed
- Renamed scripts.

### Added
- Edit mode (opens RizomUV with the most recent file instead of overwriting with the selected objects).
- Added automatic UV mapping, one click automatic trip between RizomUV and Blender using the autoseams scripts.
- More settings (packing quality and mutations).