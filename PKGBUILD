# Original Maintainer: Thibaut Sautereau (thithib) <thibaut at sautereau dot fr>
# Maintainer: Tad <tad@spotco.us>
pkgname=hardened_malloc
pkgver=12
pkgrel=7
pkgdesc="Hardened allocator designed for modern systems"
arch=('x86_64')
url="https://github.com/GrapheneOS/hardened_malloc"
license=('MIT')
depends=('gcc-libs')
makedepends=('git')
checkdepends=('python')
provides=('libhardened_malloc.so' 'libhardened_malloc-light.so')
source=("git+https://github.com/GrapheneOS/$pkgname#tag=$pkgver?signed"
	"opt.patch"
	"ld.so.preload"
	"hardened_malloc.conf"
	"LICENSE-library"
	"README.md"
	"hardened_malloc_disable.conf"
	"hardened_malloc_allow_pkey.conf"
	"hardened_malloc_helpers.sh"
	"hardened_malloc_light.conf")
sha256sums=('SKIP'
	'c85c8ab49bfb96237567a059376603e1c29ea2626d0696d86382788f2ba79f49'
	'fdbff0f87013bcfe02a3958ba1dfe62fb875127fa39f83c571b57ae0427c7b38'
	'fb0b0b97b98245a3f39c7dff824e6bb54499459ca787eed44d0e3819ae5bf1c8'
	'ac78e6c9ca0742f9112ef512dcf3a69fbfd16093f148bbbff7c04e44ae23ffed'
	'SKIP'
	'bb0abba87750662569e26d36076edaad2911c632de05b052d29f9ee5b4177081'
	'c7881757fc4fae1860026b360a820cc6436f6dc3c30a248e29ba6e7caf099cbc'
	'6828b4b329d7567903edd30e6777cff596070c49fb15b34b0ac093afef011311'
	'ef944bfe6de9d0c56d59cc2b01a6afd89282a76c3d7479b2e66cb7ce282309db')
validpgpkeys=('65EEFE022108E2B708CBFCF7F9E712E59AF5F22A') # Daniel Micay <danielmicay@gmail.com>

build() {
	cd "$pkgname"
	patch -p1 < ../opt.patch;

	ln -s default.mk config/default-x86-64.mk;
	ln -s default.mk config/default-x86-64-v2.mk;
	ln -s default.mk config/default-x86-64-v3.mk;
	ln -s default.mk config/default-x86-64-v4.mk;

	ln -s light.mk config/light-x86-64.mk;
	ln -s light.mk config/light-x86-64-v2.mk;
	ln -s light.mk config/light-x86-64-v3.mk;
	ln -s light.mk config/light-x86-64-v4.mk;

	#add a memory efficient variant
	cp config/default.mk config/memefficient.mk;
	sed -i 's/CONFIG_N_ARENA := 4/CONFIG_N_ARENA := 1/' config/memefficient.mk;
	sed -i 's/CONFIG_EXTENDED_SIZE_CLASSES := true/CONFIG_EXTENDED_SIZE_CLASSES := false/' config/memefficient.mk;
	ln -s memefficient.mk config/memefficient-x86-64.mk;
	ln -s memefficient.mk config/memefficient-x86-64-v2.mk;
	ln -s memefficient.mk config/memefficient-x86-64-v3.mk;
	ln -s memefficient.mk config/memefficient-x86-64-v4.mk;

	#add a Memory Protection Keys variant
	cp config/default.mk config/pku.mk;
	sed -i 's/CONFIG_SEAL_METADATA := false/CONFIG_SEAL_METADATA := true/' config/pku.mk;
	ln -s pku.mk config/pku-x86-64.mk;
	ln -s pku.mk config/pku-x86-64-v2.mk;
	ln -s pku.mk config/pku-x86-64-v3.mk;
	ln -s pku.mk config/pku-x86-64-v4.mk;

	make CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=default;
	make CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=default-x86-64;
	make CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=default-x86-64-v2;
	make CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=default-x86-64-v3;
	make CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=default-x86-64-v4;

	make CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=light;
	make CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=light-x86-64;
	make CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=light-x86-64-v2;
	make CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=light-x86-64-v3;
	make CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=light-x86-64-v4;

	make CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=memefficient;
	make CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=memefficient-x86-64;
	make CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v2;
	make CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v3;
	make CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v4;

	make CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=pku;
	make CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=pku-x86-64;
	make CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=pku-x86-64-v2;
	make CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=pku-x86-64-v3;
	make CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=pku-x86-64-v4;
}

package() {
	cd "$pkgname"
	install -Dm4644 "out/libhardened_malloc.so" "$pkgdir"/usr/lib/libhardened_malloc.so;
	install -Dm4644 "out-default-x86-64/libhardened_malloc-default-x86-64.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64/libhardened_malloc.so;
	install -Dm4644 "out-default-x86-64-v2/libhardened_malloc-default-x86-64-v2.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v2/libhardened_malloc.so;
	install -Dm4644 "out-default-x86-64-v3/libhardened_malloc-default-x86-64-v3.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v3/libhardened_malloc.so;
	install -Dm4644 "out-default-x86-64-v4/libhardened_malloc-default-x86-64-v4.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v4/libhardened_malloc.so;

	install -Dm4644 "out-light/libhardened_malloc-light.so" "$pkgdir"/usr/lib/libhardened_malloc-light.so;
	install -Dm4644 "out-light-x86-64/libhardened_malloc-light-x86-64.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64/libhardened_malloc-light.so;
	install -Dm4644 "out-light-x86-64-v2/libhardened_malloc-light-x86-64-v2.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v2/libhardened_malloc-light.so;
	install -Dm4644 "out-light-x86-64-v3/libhardened_malloc-light-x86-64-v3.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v3/libhardened_malloc-light.so;
	install -Dm4644 "out-light-x86-64-v4/libhardened_malloc-light-x86-64-v4.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v4/libhardened_malloc-light.so;

	install -Dm4644 "out-memefficient/libhardened_malloc-memefficient.so" "$pkgdir"/usr/lib/libhardened_malloc-memefficient.so;
	install -Dm4644 "out-memefficient-x86-64/libhardened_malloc-memefficient-x86-64.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64/libhardened_malloc-memefficient.so;
	install -Dm4644 "out-memefficient-x86-64-v2/libhardened_malloc-memefficient-x86-64-v2.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v2/libhardened_malloc-memefficient.so;
	install -Dm4644 "out-memefficient-x86-64-v3/libhardened_malloc-memefficient-x86-64-v3.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v3/libhardened_malloc-memefficient.so;
	install -Dm4644 "out-memefficient-x86-64-v4/libhardened_malloc-memefficient-x86-64-v4.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v4/libhardened_malloc-memefficient.so;

	install -Dm4644 "out-pku/libhardened_malloc-pku.so" "$pkgdir"/usr/lib/libhardened_malloc-pku.so;
	install -Dm4644 "out-pku-x86-64/libhardened_malloc-pku-x86-64.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64/libhardened_malloc-pku.so;
	install -Dm4644 "out-pku-x86-64-v2/libhardened_malloc-pku-x86-64-v2.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v2/libhardened_malloc-pku.so;
	install -Dm4644 "out-pku-x86-64-v3/libhardened_malloc-pku-x86-64-v3.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v3/libhardened_malloc-pku.so;
	install -Dm4644 "out-pku-x86-64-v4/libhardened_malloc-pku-x86-64-v4.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v4/libhardened_malloc-pku.so;

	install -Dm644 ../ld.so.preload "$pkgdir"/etc/ld.so.preload;
	install -Dm644 ../hardened_malloc.conf "$pkgdir"/etc/sysctl.d/hardened_malloc.conf;

	install -Dm644 ../LICENSE-library "$pkgdir"/usr/share/doc/hardened_malloc/LICENSE-library;
	install -Dm644 ../README.md "$pkgdir"/usr/share/doc/hardened_malloc/README.md;

	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/certbot-renew.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/php-fpm.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/libvirtd.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/virtqemud.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/user/wireplumber.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_light.conf "$pkgdir"/usr/lib/systemd/user/wireplumber.service.d/00-hardened_malloc_light.conf;

	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/fprintd.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/irqbalance.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/NetworkManager.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/polkit.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/rngd.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/upower.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/system/wpa_supplicant.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/user/pipewire-pulse.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/user/pipewire.service.d/99-hardened_malloc_allow_pkey.conf;
	#install -Dm644 ../hardened_malloc_allow_pkey.conf "$pkgdir"/usr/lib/systemd/user/wireplumber.service.d/99-hardened_malloc_allow_pkey.conf;

	install -Dm644 ../hardened_malloc_helpers.sh "$pkgdir"/etc/profile.d/hardened_malloc_helpers.sh;
}
