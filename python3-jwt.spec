#
# Conditional build:
%bcond_with	tests	# unit tests (not included in dist)

Summary:	JSON Web Token library for Python 3
Summary(pl.UTF-8):	Biblioteka JSON Web Token dla Pythona 3
Name:		python3-jwt
Version:	1.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jwt/
Source0:	https://files.pythonhosted.org/packages/source/j/jwt/jwt-%{version}.tar.gz
# Source0-md5:	d430b0a659660e43e0bd4ec92ad323d9
Patch0:		%{name}-requirements.patch
URL:		https://pypi.org/project/jwt/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 2.9.3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a JSON Web Token library for Python developed at Gehirn Inc.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę JSON Web Token dla Pythona, rozwijaną w
Gehirn Inc.

%prep
%setup -q -n jwt-%{version}
%patch0 -p1

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s jwt/tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/jwt
%{py3_sitescriptdir}/jwt-%{version}-py*.egg-info
