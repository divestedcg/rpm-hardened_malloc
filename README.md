Unofficial package for hardened_malloc
======================================

Overview
--------
This repo contains an RPM specfile and a PKGBUILD for micro-architecture optimized builds of the hardened_malloc library.

Upstream Project
----------------
- https://github.com/GrapheneOS/hardened_malloc
	- Donate:
		- https://grapheneos.org/donate
		- https://github.com/sponsors/thestinger

Compatibility
-------------
- Fedora 40/41/42/etc.
- Arch Linux

Prebuilts
---------
- Fedora via Divested-RPM: https://divested.dev/index.php?page=software#divested-release
- Fedora via CI: https://gitlab.com/divested/rpm-hardened_malloc/-/jobs/artifacts/master/browse?job=build_rpm
- Arch via CI: TODO

Modifications
-------------
- mseal is used for some allocator data
	- https://github.com/GrapheneOS/hardened_malloc/pull/242
- memcpy/memmove/memset are overridden to perform size checks, experimental
	- https://github.com/GrapheneOS/hardened_malloc/pull/252

Included Variants
-----------------
Four variants are included compiled for four different micro-architectures:

- mpk
	- prioritizes security, passes all tests
		- protects allocator metadata using Memory Protection Keys
		- needs processor support: `grep -q " pku " /proc/cpuinfo && echo "Supported" || echo "Not supported"`
		- incompatible with systemd's default seccomp filter, no easy way to override
- default
	- prioritizes security, passes all tests
- memefficient
	- prioritizes memory usage, passes all tests
		- decreases arenas used from 4 to 1
		- disables extended size classes
- light
	- prioritizes CPU and memory usage, fails six tests
		- disables slab quarantines
		- disables write after free check
		- disables slot randomization
		- raises the guard slab interval from 1 to 8

The default is chosen at install time depending:
- 12GB+ RAM: -default
- <12GB RAM: -memefficient

Known Issues
------------
- Firefox/Tor Browser/etc.
	- Workaround: add `blacklist /etc/ld.so.preload` to their firejail profiles
	- Our patched firejail available via Divested-RPM includes this workaround
- certbot segfaults consistently
	- Workaround included for certbot-renew systemd service
	- 2023/11/26: can't reproduce anymore, maybe fixed
- php-fpm
	- Workaround included for php-fpm systemd service
- virtiofs will stall out if used on host
	- Workaround included for virtqemud systemd service
- qemu with virgl enabled will sometimes randomly segfault
- nautilus will randomly segfault when navigating directory trees too quickly
	- This seems to happen even without hm
- wireplumber 0.4.16 has a write after free issue
	- Fixed in 0.4.17
	- https://gitlab.freedesktop.org/pipewire/wireplumber/-/issues/534
- gnome-control-center <=45.1 has a write after free issue
	- Fixed in 45.2
	- Avoid the privacy settings tab
	- https://gitlab.gnome.org/GNOME/gnome-control-center/-/merge_requests/2012
	- https://bugzilla.redhat.com/show_bug.cgi?id=2230571
- libhandy <=1.8.2 has a write after free issue
	- Fedora fixed in libhandy-1.8.2-5.fc39
	- https://bugzilla.redhat.com/show_bug.cgi?id=2253814
- liferea <1.15.9 has a write after free issue
- dnf may crash on large transactions, especially (offline) system-upgrade
	- please disable/remove it temporarily before invoking the update
- There is an included `nohm` alias to start programs without it
- You can also fetch journald output with `gethmlogs` or `gethmlogsall` for current boot or all boots respectively

License
-------
MIT

Credits
-------
- @GrapheneOS for the hardened_malloc project itself
- @noatsecure/HardHatOS for the original RPM specfile
- @thithib for the original PKGBUILD
- Whonix for the bubblewrap command to disable the preload
