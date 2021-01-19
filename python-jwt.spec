#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	JSON Web Token library for Python 2
Summary(pl.UTF-8):	Biblioteka JSON Web Token dla Pythona 2
Name:		python-jwt
Version:	0.3.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jwt/
Source0:	https://files.pythonhosted.org/packages/source/j/jwt/jwt-%{version}.tar.gz
# Source0-md5:	97deed6b354bc8f5163f6a5cbe6c849e
URL:		https://pypi.org/project/jwt/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Crypto = 2.6.1
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Crypto = 2.6.1
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a JSON Web Token library for Python developed at Gehirn Inc.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę JSON Web Token dla Pythona, rozwijaną w
Gehirn Inc.

%package -n python3-jwt
Summary:	JSON Web Token library for Python 3
Summary(pl.UTF-8):	Biblioteka JSON Web Token dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-jwt
This is a JSON Web Token library for Python developed at Gehirn Inc.

%description -n python3-jwt -l pl.UTF-8
Ten pakiet zawiera bibliotekę JSON Web Token dla Pythona, rozwijaną w
Gehirn Inc.

%prep
%setup -q -n jwt-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s jwt/tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s jwt/tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/jwt
%{py_sitescriptdir}/jwt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jwt
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/jwt
%{py3_sitescriptdir}/jwt-%{version}-py*.egg-info
%endif
