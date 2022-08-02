BuildArch: x86_64
BuildRequires: gcc, gcc-c++, make
License: MIT
Name: hardened_malloc
Release: 17%{?dist}
Source0: https://api.github.com/repos/GrapheneOS/hardened_malloc/tarball/11
Source1: opt.patch
Source2: ld.so.preload
Source3: hardened_malloc.conf
Source4: LICENSE-library
Source5: LICENSE-spec
Source6: README.md
Summary: Hardened memory allocator from GrapheneOS
URL: https://github.com/GrapheneOS/hardened_malloc
Version: 11

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

#add a memory efficient variant, based on light with perf impactful features re-enabled
cp config/light.mk config/memefficient.mk;
sed -i 's/CONFIG_WRITE_AFTER_FREE_CHECK := false/CONFIG_WRITE_AFTER_FREE_CHECK := true/' config/memefficient.mk;
sed -i 's/CONFIG_SLOT_RANDOMIZE := false/CONFIG_SLOT_RANDOMIZE := true/' config/memefficient.mk;
ln -s memefficient.mk config/memefficient-x86-64.mk;
ln -s memefficient.mk config/memefficient-x86-64-v2.mk;
ln -s memefficient.mk config/memefficient-x86-64-v3.mk;
ln -s memefficient.mk config/memefficient-x86-64-v4.mk;

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

install -Dm644 "%{SOURCE2}" %{buildroot}%{_sysconfdir}/ld.so.preload;
install -Dm644 "%{SOURCE3}" %{buildroot}%{_sysconfdir}/sysctl.d/hardened_malloc.conf;

install -Dm644 "%{SOURCE4}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-library;
install -Dm644 "%{SOURCE5}" %{buildroot}/usr/share/doc/hardened_malloc/LICENSE-spec;
install -Dm644 "%{SOURCE6}" %{buildroot}/usr/share/doc/hardened_malloc/README.md;

%files
%{_sysconfdir}/ld.so.preload
%{_sysconfdir}/sysctl.d/hardened_malloc.conf
/lib64/libhardened_malloc.so
/lib64/libhardened_malloc-light.so
/lib64/libhardened_malloc-memefficient.so
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
/usr/share/doc/hardened_malloc/LICENSE-library
/usr/share/doc/hardened_malloc/LICENSE-spec
/usr/share/doc/hardened_malloc/README.md
