#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-poetry_plugin_export
Version  : 1.3.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/48/13/47dfed5231a975a0ee2bbb936638b71057b8b2c87ea1f010c37c83858ad1/poetry_plugin_export-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/13/47dfed5231a975a0ee2bbb936638b71057b8b2c87ea1f010c37c83858ad1/poetry_plugin_export-1.3.0.tar.gz
Summary  : Poetry plugin to export the dependencies to various formats
Group    : Development/Tools
License  : MIT
Requires: pypi-poetry_plugin_export-license = %{version}-%{release}
Requires: pypi-poetry_plugin_export-python = %{version}-%{release}
Requires: pypi-poetry_plugin_export-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Poetry Plugin: Export
This package is a plugin that allows the export of locked packages to various formats.

%package license
Summary: license components for the pypi-poetry_plugin_export package.
Group: Default

%description license
license components for the pypi-poetry_plugin_export package.


%package python
Summary: python components for the pypi-poetry_plugin_export package.
Group: Default
Requires: pypi-poetry_plugin_export-python3 = %{version}-%{release}

%description python
python components for the pypi-poetry_plugin_export package.


%package python3
Summary: python3 components for the pypi-poetry_plugin_export package.
Group: Default
Requires: python3-core
Provides: pypi(poetry_plugin_export)
Requires: pypi(poetry)
Requires: pypi(poetry_core)

%description python3
python3 components for the pypi-poetry_plugin_export package.


%prep
%setup -q -n poetry_plugin_export-1.3.0
cd %{_builddir}/poetry_plugin_export-1.3.0
pushd ..
cp -a poetry_plugin_export-1.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675116246
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-poetry_plugin_export
cp %{_builddir}/poetry_plugin_export-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_plugin_export/3a0e7a4afb831c908ab41b8bb1787ecc183ebc5c || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-poetry_plugin_export/3a0e7a4afb831c908ab41b8bb1787ecc183ebc5c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
