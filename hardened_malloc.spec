BuildArch: x86_64
BuildRequires: gcc, gcc-c++, make
License: MIT
Name: hardened_malloc
Release: 9%{?dist}
Source0: https://api.github.com/repos/GrapheneOS/hardened_malloc/tarball/12
Source1: opt.patch
Source2: ld.so.preload
Source3: hardened_malloc.conf
Source4: LICENSE-library
Source5: LICENSE-spec
Source6: README.md
Source7: hardened_malloc_disable.conf
Source8: hardened_malloc_allow_pkey.conf
Source9: hardened_malloc_helpers.sh
Source10: hardened_malloc_light.conf
Summary: Hardened memory allocator from GrapheneOS
URL: https://github.com/GrapheneOS/hardened_malloc
Version: 12

%description
Hardened allocator designed for modern systems

%prep
%define _srcdir hardened_malloc

%{__mkdir} %{_srcdir};
%{__tar} -x -f %{SOURCE0} -C %{_srcdir} --strip-components 1;

%build
cd %{_srcdir};
#optimizations
patch -p1 < %{SOURCE1};

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

%{__make} CONFIG_NATIVE=false CONFIG_WERROR=false VARIANT=pku;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64=true CONFIG_WERROR=false VARIANT=pku-x86-64;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V2=true CONFIG_WERROR=false VARIANT=pku-x86-64-v2;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V3=true CONFIG_WERROR=false VARIANT=pku-x86-64-v3;
%{__make} CONFIG_NATIVE=false CONFIG_X86_64_V4=true CONFIG_WERROR=false VARIANT=pku-x86-64-v4;

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

install -Dm4644 "%{_srcdir}/out-pku/libhardened_malloc-pku.so" %{buildroot}/lib64/libhardened_malloc-pku.so;
install -Dm4644 "%{_srcdir}/out-pku-x86-64/libhardened_malloc-pku-x86-64.so" %{buildroot}/lib64/glibc-hwcaps/x86-64/libhardened_malloc-pku.so;
install -Dm4644 "%{_srcdir}/out-pku-x86-64-v2/libhardened_malloc-pku-x86-64-v2.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-pku.so;
install -Dm4644 "%{_srcdir}/out-pku-x86-64-v3/libhardened_malloc-pku-x86-64-v3.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-pku.so;
install -Dm4644 "%{_srcdir}/out-pku-x86-64-v4/libhardened_malloc-pku-x86-64-v4.so" %{buildroot}/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-pku.so;

install -Dm644 "%{SOURCE2}" %{buildroot}%{_sysconfdir}/ld.so.preload;
install -Dm644 "%{SOURCE3}" %{buildroot}%{_sysconfdir}/sysctl.d/hardened_malloc.conf;

install -Dm644 "%{SOURCE4}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-library;
install -Dm644 "%{SOURCE5}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-spec;
install -Dm644 "%{SOURCE6}" %{buildroot}/usr/share/doc/hardened_malloc/README.md;

install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/certbot-renew.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/php-fpm.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/libvirtd.service.d/00-hardened_malloc_disable.conf;
install -Dm644 "%{SOURCE7}" %{buildroot}/usr/lib/systemd/system/virtqemud.service.d/00-hardened_malloc_disable.conf;

install -Dm644 "%{SOURCE10}" %{buildroot}/usr/lib/systemd/user/gnome-terminal-server.service.d/00-hardened_malloc_light.conf;

#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/fprintd.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/irqbalance.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/NetworkManager.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/polkit.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/rngd.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/upower.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/system/wpa_supplicant.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/user/pipewire-pulse.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/user/pipewire.service.d/99-hardened_malloc_allow_pkey.conf;
#install -Dm644 "%{SOURCE8}" %{buildroot}/usr/lib/systemd/user/wireplumber.service.d/99-hardened_malloc_allow_pkey.conf;

install -Dm644 "%{SOURCE9}" %{buildroot}/etc/profile.d/hardened_malloc_helpers.sh;

%files
%{_sysconfdir}/ld.so.preload
%{_sysconfdir}/sysctl.d/hardened_malloc.conf
/lib64/libhardened_malloc.so
/lib64/libhardened_malloc-light.so
/lib64/libhardened_malloc-memefficient.so
/lib64/libhardened_malloc-pku.so
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
/lib64/glibc-hwcaps/x86-64/libhardened_malloc-pku.so
/lib64/glibc-hwcaps/x86-64-v2/libhardened_malloc-pku.so
/lib64/glibc-hwcaps/x86-64-v3/libhardened_malloc-pku.so
/lib64/glibc-hwcaps/x86-64-v4/libhardened_malloc-pku.so
/usr/share/doc/hardened_malloc/LICENSE-library
/usr/share/doc/hardened_malloc/LICENSE-spec
/usr/share/doc/hardened_malloc/README.md
/usr/lib/systemd/*/*/*.conf
/etc/profile.d/hardened_malloc_helpers.sh
