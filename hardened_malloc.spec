BuildArch: x86_64
BuildRequires: gcc, gcc-c++, make
License: MIT
Name: hardened_malloc
Release: 5%{?dist}
Source0: https://api.github.com/repos/GrapheneOS/hardened_malloc/tarball/2025012700
Source1: 0001-opt.patch
Source2: 0002-graceful_pkey.patch
Source3: hardened_malloc.conf
Source4: LICENSE-library
Source5: LICENSE-spec
Source6: README.md
Source7: hardened_malloc_disable.conf
Source8: hardened_malloc_helpers.sh
Source9: 0242-mseal.patch
Source10: 0252-blockops-size.patch
Summary: Hardened memory allocator from GrapheneOS
URL: https://github.com/GrapheneOS/hardened_malloc
Version: 2025012700

%description
Hardened allocator designed for modern systems

%posttrans
totalRAM=$(free -m | awk '/^Mem:/{print $2}');
if [ "$totalRAM" -gt "11500" ]; then
#if grep -q " pku " /proc/cpuinfo; then
#echo "Enabling hardened_malloc with -mpk variant";
#echo "libhardened_malloc-mpk.so" > /etc/ld.so.preload;
#else
echo "Enabling hardened_malloc with -default variant";
echo "libhardened_malloc.so" > /etc/ld.so.preload;
#fi;
else
echo "Enabling hardened_malloc with -memefficient variant";
echo "libhardened_malloc-memefficient.so" > /etc/ld.so.preload;
fi;

%preun
if [ "$1" == "0" ]; then
echo "Removing ld.so.preload";
rm /etc/ld.so.preload;
fi;

%prep
%define _srcdir hardened_malloc

%{__mkdir} %{_srcdir};
%{__tar} -x -f %{SOURCE0} -C %{_srcdir} --strip-components 1;

%build
cd %{_srcdir};
#optimizations
patch -p1 < %{SOURCE1};
#patch -p1 < %{SOURCE2};
patch -p1 < %{SOURCE9};
patch -p1 < %{SOURCE10};

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

#add a variant that checks sizes of select block operations
cp config/default.mk config/bos.mk;
sed -i 's/CONFIG_BLOCK_OPS_CHECK_SIZE := false/CONFIG_BLOCK_OPS_CHECK_SIZE := true/' config/bos.mk;
ln -s bos.mk config/bos-x86-64.mk;
ln -s bos.mk config/bos-x86-64-v2.mk;
ln -s bos.mk config/bos-x86-64-v3.mk;
ln -s bos.mk config/bos-x86-64-v4.mk;

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=default;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=default-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=default-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=default-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=default-x86-64-v4;

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=light;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=light-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=light-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=light-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=light-x86-64-v4;

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=memefficient;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=memefficient-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=memefficient-x86-64-v4;

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=mpk;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=mpk-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=mpk-x86-64-v4;

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=bos;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=bos-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=bos-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=bos-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=bos-x86-64-v4;

%install
install -Dm4644 "%{_srcdir}/out/libhardened_malloc.so" %{buildroot}/lib64/libhardened_malloc.so;
install -Dm4644 "%{_srcdir}/out-default-x86-64/libhardened_malloc-default-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc.so;
install -Dm4644 "%{_srcdir}/out-default-x86-64-v2/libhardened_malloc-default-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc.so;
install -Dm4644 "%{_srcdir}/out-default-x86-64-v3/libhardened_malloc-default-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc.so;
install -Dm4644 "%{_srcdir}/out-default-x86-64-v4/libhardened_malloc-default-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc.so;

install -Dm4644 "%{_srcdir}/out-light/libhardened_malloc-light.so" %{buildroot}/lib64/libhardened_malloc-light.so;
install -Dm4644 "%{_srcdir}/out-light-x86-64/libhardened_malloc-light-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc-light.so;
install -Dm4644 "%{_srcdir}/out-light-x86-64-v2/libhardened_malloc-light-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-light.so;
install -Dm4644 "%{_srcdir}/out-light-x86-64-v3/libhardened_malloc-light-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-light.so;
install -Dm4644 "%{_srcdir}/out-light-x86-64-v4/libhardened_malloc-light-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-light.so;

install -Dm4644 "%{_srcdir}/out-memefficient/libhardened_malloc-memefficient.so" %{buildroot}/lib64/libhardened_malloc-memefficient.so;
install -Dm4644 "%{_srcdir}/out-memefficient-x86-64/libhardened_malloc-memefficient-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc-memefficient.so;
install -Dm4644 "%{_srcdir}/out-memefficient-x86-64-v2/libhardened_malloc-memefficient-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-memefficient.so;
install -Dm4644 "%{_srcdir}/out-memefficient-x86-64-v3/libhardened_malloc-memefficient-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-memefficient.so;
install -Dm4644 "%{_srcdir}/out-memefficient-x86-64-v4/libhardened_malloc-memefficient-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-memefficient.so;

install -Dm4644 "%{_srcdir}/out-mpk/libhardened_malloc-mpk.so" %{buildroot}/lib64/libhardened_malloc-mpk.so;
install -Dm4644 "%{_srcdir}/out-mpk-x86-64/libhardened_malloc-mpk-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc-mpk.so;
install -Dm4644 "%{_srcdir}/out-mpk-x86-64-v2/libhardened_malloc-mpk-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-mpk.so;
install -Dm4644 "%{_srcdir}/out-mpk-x86-64-v3/libhardened_malloc-mpk-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-mpk.so;
install -Dm4644 "%{_srcdir}/out-mpk-x86-64-v4/libhardened_malloc-mpk-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-mpk.so;

install -Dm4644 "%{_srcdir}/out-bos/libhardened_malloc-bos.so" %{buildroot}/lib64/libhardened_malloc-bos.so;
install -Dm4644 "%{_srcdir}/out-bos-x86-64/libhardened_malloc-bos-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc-bos.so;
install -Dm4644 "%{_srcdir}/out-bos-x86-64-v2/libhardened_malloc-bos-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-bos.so;
install -Dm4644 "%{_srcdir}/out-bos-x86-64-v3/libhardened_malloc-bos-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-bos.so;
install -Dm4644 "%{_srcdir}/out-bos-x86-64-v4/libhardened_malloc-bos-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-bos.so;

install -Dm644 "%{SOURCE3}" %{buildroot}%{_sysconfdir}/sysctl.d/hardened_malloc.conf;

install -Dm644 "%{SOURCE4}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-library;
install -Dm644 "%{SOURCE5}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-spec;
install -Dm644 "%{SOURCE6}" %{buildroot}/usr/share/doc/hardened_malloc/README.md;

install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/certbot-renew.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/php-fpm.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/libvirtd.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/virtqemud.service.d/00-hardened_malloc_disable.conf;

install -Dm644 "%{SOURCE8}" %{buildroot}/etc/profile.d/hardened_malloc_helpers.sh;

%files
%{_sysconfdir}/sysctl.d/hardened_malloc.conf
/lib64/libhardened_malloc.so
/lib64/libhardened_malloc-light.so
/lib64/libhardened_malloc-memefficient.so
/lib64/libhardened_malloc-mpk.so
/lib64/libhardened_malloc-bos.so
/lib64/glibc-hwcaps/x86-64/libhardened_malloc.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc.so
/lib64/glibc-hwcaps/x86-64/libhardened_malloc-light.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-light.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-light.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-light.so
/lib64/glibc-hwcaps/x86-64/libhardened_malloc-memefficient.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-memefficient.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-memefficient.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-memefficient.so
/lib64/glibc-hwcaps/x86-64/libhardened_malloc-mpk.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-mpk.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-mpk.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-mpk.so
/lib64/glibc-hwcaps/x86-64/libhardened_malloc-bos.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-bos.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-bos.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-bos.so
/usr/share/doc/hardened_malloc/LICENSE-library
/usr/share/doc/hardened_malloc/LICENSE-spec
/usr/share/doc/hardened_malloc/README.md
/usr/lib/systemd/*/*/*.conf
/etc/profile.d/hardened_malloc_helpers.sh
