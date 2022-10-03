#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-poetry_plugin_export
Version  : 1.1.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/2c/3c/0d2d1043b092ac901343f99f060b7e231fb091f8bdd3bc36e6a72cf4a8c3/poetry-plugin-export-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2c/3c/0d2d1043b092ac901343f99f060b7e231fb091f8bdd3bc36e6a72cf4a8c3/poetry-plugin-export-1.1.1.tar.gz
Summary  : Poetry plugin to export the dependencies to various formats
Group    : Development/Tools
License  : MIT
Requires: pypi-poetry_plugin_export-license = %{version}-%{release}
Requires: pypi-poetry_plugin_export-python = %{version}-%{release}
Requires: pypi-poetry_plugin_export-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

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
%setup -q -n poetry-plugin-export-1.1.1
cd %{_builddir}/poetry-plugin-export-1.1.1
pushd ..
cp -a poetry-plugin-export-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664830406
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-poetry_plugin_export
cp %{_builddir}/poetry-plugin-export-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-poetry_plugin_export/3a0e7a4afb831c908ab41b8bb1787ecc183ebc5c || :
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
