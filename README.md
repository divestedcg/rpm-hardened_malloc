Package for hardened_malloc
===========================

Overview
--------
This repo contains an RPM specfile and a PKGBUILD for multiarchitecture optimized builds of the hardened_malloc library.

Upstream Project
----------------
- https://github.com/GrapheneOS/hardened_malloc

Compatibility
-------------
- Fedora 36
- Arch Linux

Prebuilts
---------
- via Divested-RPM: https://divested.dev/index.php?page=software#divested-release
- via CI: https://gitlab.com/divested/rpm-hardened_malloc/-/jobs/artifacts/master/browse?job=build_rpm

Known Incompatibilities
-----------------------
- Firefox/Tor Browser/etc.
	- Workaround: add `blacklist /etc/ld.so.preload` to their firejail profiles
	- Our patched firejail available via Divested-RPM includes this workaround
- php-fpm
	- Workaround: add `InaccessiblePaths=-/etc/ld.so.preload` to a systemd unit override
	- Our brace includes this workaround

License
-------
MIT

Credits
-------
- @noatsecure/HardHatOS for the original RPM specfile
- @thithib for the original PKGBUILD
