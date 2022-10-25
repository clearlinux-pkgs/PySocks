#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PySocks
Version  : 1.7.0
Release  : 25
URL      : https://github.com/Anorov/PySocks/archive/1.7.0/PySocks-1.7.0.tar.gz
Source0  : https://github.com/Anorov/PySocks/archive/1.7.0/PySocks-1.7.0.tar.gz
Summary  : A Python SOCKS client module. See https://github.com/Anorov/PySocks for more information.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: PySocks-license = %{version}-%{release}
Requires: PySocks-python = %{version}-%{release}
Requires: PySocks-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
PySocks
=======
PySocks lets you send traffic through SOCKS and HTTP proxy servers. It is a modern fork of [SocksiPy](http://socksipy.sourceforge.net/) with bug fixes and extra features.

%package license
Summary: license components for the PySocks package.
Group: Default

%description license
license components for the PySocks package.


%package python
Summary: python components for the PySocks package.
Group: Default
Requires: PySocks-python3 = %{version}-%{release}
Provides: pysocks-python

%description python
python components for the PySocks package.


%package python3
Summary: python3 components for the PySocks package.
Group: Default
Requires: python3-core
Provides: pypi(pysocks)

%description python3
python3 components for the PySocks package.


%prep
%setup -q -n PySocks-1.7.0
cd %{_builddir}/PySocks-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644185434
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PySocks
cp %{_builddir}/PySocks-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/PySocks/553bbf60cec5702a5b3a4e23a70e72322fbec333
cp %{_builddir}/PySocks-1.7.0/test/bin/3proxy.license %{buildroot}/usr/share/package-licenses/PySocks/d122c44dcbd4bc9b0e1474b3f46d468bb6d8050c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PySocks/553bbf60cec5702a5b3a4e23a70e72322fbec333
/usr/share/package-licenses/PySocks/d122c44dcbd4bc9b0e1474b3f46d468bb6d8050c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
