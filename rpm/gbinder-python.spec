%define _proj_name gbinder
%define modname %{_proj_name}
%define fedname %{modname}
%define internal_name gbinder

Name: python-%{modname}
Version: 1.3.1
Release: 1
License: GPLv3
Summary: Python bindings for libgbinder

BuildRequires: gcc
BuildRequires: libgbinder-devel libglibutil-devel pkgconfig

Source: %{name}-%{version}.tar.gz
%if 0%{sailfishos_version} <= 50000
Patch0: 001-no-noexcept.patch
%endif

%description
Cython extension module for gbinder

%package -n python3-%{fedname}
Summary: %{summary}
BuildRequires: python3-devel python3-setuptools
BuildRequires: python3-cython
BuildRequires: python-rpm-macros
%{?python_provide:%python_provide python3-%{fedname}}
%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{fedname} 
%{description}

Python 3 version.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%{python3} ./setup.py build_ext --inplace --cython
env WITH_CYTHON=true %{py3_build}

%install
%{py3_install}

%files -n python3-%{fedname}
%{python3_sitearch}/%{internal_name}*.so
%{python3_sitearch}/%{internal_name}*.egg-info
