# Original Maintainer: Thibaut Sautereau (thithib) <thibaut at sautereau dot fr>
# Maintainer: Tad <tad@spotco.us>
pkgname=hardened_malloc
pkgver=2025012700
pkgrel=1
pkgdesc="Hardened allocator designed for modern systems"
arch=('x86_64')
url="https://github.com/GrapheneOS/hardened_malloc"
license=('MIT')
depends=('gcc-libs')
makedepends=('git')
checkdepends=('python')
provides=('libhardened_malloc.so' 'libhardened_malloc-light.so')
source=("git+https://github.com/GrapheneOS/$pkgname#tag=$pkgver?signed"
	"0001-opt.patch"
	"0002-graceful_pkey.patch"
	"0242-mseal.patch"
	"ld.so.preload"
	"hardened_malloc.conf"
	"LICENSE-library"
	"README.md"
	"hardened_malloc_disable.conf"
	"hardened_malloc_helpers.sh")
sha256sums=('SKIP'
	'c85c8ab49bfb96237567a059376603e1c29ea2626d0696d86382788f2ba79f49'
	'9af3b434d273ba93840ee613fb36cacd947dfc8a73fbee42e049869becf6f1d0'
	'c345f3a5f6a6f68fe8bebe3c09980b985073aa3260ae3039cb9867952be20410'
	'fdbff0f87013bcfe02a3958ba1dfe62fb875127fa39f83c571b57ae0427c7b38'
	'926f23b9470143bcbba942025c2bdfd551840fd539c1e8fa05fbe67b97959e76'
	'ac78e6c9ca0742f9112ef512dcf3a69fbfd16093f148bbbff7c04e44ae23ffed'
	'SKIP'
	'bb0abba87750662569e26d36076edaad2911c632de05b052d29f9ee5b4177081'
	'c7881757fc4fae1860026b360a820cc6436f6dc3c30a248e29ba6e7caf099cbc'
	'6828b4b329d7567903edd30e6777cff596070c49fb15b34b0ac093afef011311'
	'1abccc05eb05dbd17542f93342f51b4d70dcb0bcd019c1c9eae37a0bc5849da9')
validpgpkeys=('65EEFE022108E2B708CBFCF7F9E712E59AF5F22A') # Daniel Micay <danielmicay@gmail.com>
install=hardened_malloc.install

build() {
	cd "$pkgname"
	patch -p1 < ../0001-opt.patch;
	#patch -p1 < ../0002-graceful_pkey.patch;
	patch -p1 < ../0242-mseal.patch;

	#enable UBsan in all variants
	#sed -i 's/CONFIG_UBSAN := false/CONFIG_UBSAN := true/' config/*.mk;

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
	cp config/default.mk config/mpk.mk;
	sed -i 's/CONFIG_SEAL_METADATA := false/CONFIG_SEAL_METADATA := true/' config/mpk.mk;
	ln -s mpk.mk config/mpk-x86-64.mk;
	ln -s mpk.mk config/mpk-x86-64-v2.mk;
	ln -s mpk.mk config/mpk-x86-64-v3.mk;
	ln -s mpk.mk config/mpk-x86-64-v4.mk;

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

	make CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=mpk;
	make CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=mpk-x86-64;
	make CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v2;
	make CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v3;
	make CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v4;
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

	install -Dm4644 "out-mpk/libhardened_malloc-mpk.so" "$pkgdir"/usr/lib/libhardened_malloc-mpk.so;
	install -Dm4644 "out-mpk-x86-64/libhardened_malloc-mpk-x86-64.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64/libhardened_malloc-mpk.so;
	install -Dm4644 "out-mpk-x86-64-v2/libhardened_malloc-mpk-x86-64-v2.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v2/libhardened_malloc-mpk.so;
	install -Dm4644 "out-mpk-x86-64-v3/libhardened_malloc-mpk-x86-64-v3.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v3/libhardened_malloc-mpk.so;
	install -Dm4644 "out-mpk-x86-64-v4/libhardened_malloc-mpk-x86-64-v4.so" "$pkgdir"/usr/lib/glibc-hwcaps/x86-64-v4/libhardened_malloc-mpk.so;

	install -Dm644 ../ld.so.preload "$pkgdir"/etc/ld.so.preload;
	install -Dm644 ../hardened_malloc.conf "$pkgdir"/etc/sysctl.d/hardened_malloc.conf;

	install -Dm644 ../LICENSE-library "$pkgdir"/usr/share/doc/hardened_malloc/LICENSE-library;
	install -Dm644 ../README.md "$pkgdir"/usr/share/doc/hardened_malloc/README.md;

	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/certbot-renew.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/php-fpm.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/libvirtd.service.d/00-hardened_malloc_disable.conf;
	install -Dm644 ../hardened_malloc_disable.conf "$pkgdir"/usr/lib/systemd/system/virtqemud.service.d/00-hardened_malloc_disable.conf;

	install -Dm644 ../hardened_malloc_helpers.sh "$pkgdir"/etc/profile.d/hardened_malloc_helpers.sh;
}
