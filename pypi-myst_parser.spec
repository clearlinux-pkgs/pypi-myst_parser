#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-myst_parser
Version  : 2.0.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/e8/c1/48ea47b78ade0bb0281f34c9e343e3ea0c681fbc81464dbfd134e983954f/myst_parser-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/c1/48ea47b78ade0bb0281f34c9e343e3ea0c681fbc81464dbfd134e983954f/myst_parser-2.0.0.tar.gz
Summary  : An extended [CommonMark](https://spec.commonmark.org/) compliant parser,
Group    : Development/Tools
License  : MIT
Requires: pypi-myst_parser-bin = %{version}-%{release}
Requires: pypi-myst_parser-license = %{version}-%{release}
Requires: pypi-myst_parser-python = %{version}-%{release}
Requires: pypi-myst_parser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# MyST-Parser
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]
[![Conda][conda-badge]][conda-link]
[![PyPI - Downloads][install-badge]][install-link]

%package bin
Summary: bin components for the pypi-myst_parser package.
Group: Binaries
Requires: pypi-myst_parser-license = %{version}-%{release}

%description bin
bin components for the pypi-myst_parser package.


%package license
Summary: license components for the pypi-myst_parser package.
Group: Default

%description license
license components for the pypi-myst_parser package.


%package python
Summary: python components for the pypi-myst_parser package.
Group: Default
Requires: pypi-myst_parser-python3 = %{version}-%{release}

%description python
python components for the pypi-myst_parser package.


%package python3
Summary: python3 components for the pypi-myst_parser package.
Group: Default
Requires: python3-core
Provides: pypi(myst_parser)
Requires: pypi(docutils)
Requires: pypi(jinja2)
Requires: pypi(markdown_it_py)
Requires: pypi(mdit_py_plugins)
Requires: pypi(pyyaml)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-myst_parser package.


%prep
%setup -q -n myst_parser-2.0.0
cd %{_builddir}/myst_parser-2.0.0
pushd ..
cp -a myst_parser-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686714448
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
pypi-dep-fix.py . markdown-it-py
pypi-dep-fix.py . mdit-py-plugins
pypi-dep-fix.py . sphinx
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . docutils
pypi-dep-fix.py . markdown-it-py
pypi-dep-fix.py . mdit-py-plugins
pypi-dep-fix.py . sphinx
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-myst_parser
cp %{_builddir}/myst_parser-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-myst_parser/ab5a711cce75e49bdbd08bbcb728262e30580e5d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} docutils
pypi-dep-fix.py %{buildroot} markdown-it-py
pypi-dep-fix.py %{buildroot} mdit-py-plugins
pypi-dep-fix.py %{buildroot} sphinx
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

%files bin
%defattr(-,root,root,-)
/usr/bin/myst-anchors
/usr/bin/myst-docutils-demo
/usr/bin/myst-docutils-html
/usr/bin/myst-docutils-html5
/usr/bin/myst-docutils-latex
/usr/bin/myst-docutils-pseudoxml
/usr/bin/myst-docutils-xml
/usr/bin/myst-inv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-myst_parser/ab5a711cce75e49bdbd08bbcb728262e30580e5d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
