#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libslirp
Version  : 4.6.1
Release  : 1
URL      : https://gitlab.freedesktop.org/slirp/libslirp/uploads/83b199ea6fcdfc0c243dfde8546ee4c9/libslirp-4.6.1.tar.xz
Source0  : https://gitlab.freedesktop.org/slirp/libslirp/uploads/83b199ea6fcdfc0c243dfde8546ee4c9/libslirp-4.6.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libslirp-lib = %{version}-%{release}
Requires: libslirp-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : pkgconfig(glib-2.0)

%description
# libslirp
libslirp is a user-mode networking library used by virtual machines,
containers or various tools.

%package dev
Summary: dev components for the libslirp package.
Group: Development
Requires: libslirp-lib = %{version}-%{release}
Provides: libslirp-devel = %{version}-%{release}
Requires: libslirp = %{version}-%{release}

%description dev
dev components for the libslirp package.


%package lib
Summary: lib components for the libslirp package.
Group: Libraries
Requires: libslirp-license = %{version}-%{release}

%description lib
lib components for the libslirp package.


%package license
Summary: license components for the libslirp package.
Group: Default

%description license
license components for the libslirp package.


%prep
%setup -q -n libslirp-4.6.1
cd %{_builddir}/libslirp-4.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643072967
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libslirp
cp %{_builddir}/libslirp-4.6.1/COPYRIGHT %{buildroot}/usr/share/package-licenses/libslirp/051935530e6be28baed83b2aafe66ee5b347d656
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/slirp/libslirp-version.h
/usr/include/slirp/libslirp.h
/usr/lib64/libslirp.so
/usr/lib64/pkgconfig/slirp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libslirp.so.0
/usr/lib64/libslirp.so.0.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libslirp/051935530e6be28baed83b2aafe66ee5b347d656
