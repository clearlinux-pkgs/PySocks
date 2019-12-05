#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PySocks
Version  : 1.6.7
Release  : 5
URL      : https://github.com/Anorov/PySocks/archive/1.6.7.tar.gz
Source0  : https://github.com/Anorov/PySocks/archive/1.6.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: PySocks-license = %{version}-%{release}
Requires: PySocks-python = %{version}-%{release}
Requires: PySocks-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
PySocks
=======
Updated and semi-actively maintained version of [SocksiPy](http://socksipy.sourceforge.net/), with bug fixes and extra features.

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

%description python3
python3 components for the PySocks package.


%prep
%setup -q -n PySocks-1.6.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549570690
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PySocks
cp LICENSE %{buildroot}/usr/share/package-licenses/PySocks/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PySocks/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
