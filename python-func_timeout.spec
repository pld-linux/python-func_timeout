# TODO: GootTests based tests
#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python module to support running any existing function with a given timeout
Summary(pl.UTF-8):	Moduł Pythona pozwalający uruchamiać istniejące funkcje z podanym limitem czasu
Name:		python-func_timeout
Version:	4.3.5
Release:	6
License:	LGPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/func-timeout/
Source0:	https://files.pythonhosted.org/packages/source/f/func-timeout/func_timeout-%{version}.tar.gz
# Source0-md5:	3535d4e00d54e36757ba7c65f20e4c91
URL:		https://pypi.org/project/func-timeout/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
#BuildRequires:	python-GoodTests
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-GoodTests
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module which allows you to specify timeouts when calling any
existing function. Also provides support for stoppable-threads.

%description -l pl.UTF-8
Moduł Pythona pozwalający na określenie limitów czasu przy wywoływaniu
dowolnej istniejącej funkcji. Obsługuje także zatrzymywanie wątków.

%package -n python3-func_timeout
Summary:	Python module to support running any existing function with a given timeout
Summary(pl.UTF-8):	Moduł Pythona pozwalający uruchamiać istniejące funkcje z podanym limitem czasu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-func_timeout
Python module which allows you to specify timeouts when calling any
existing function. Also provides support for stoppable-threads.

%description -n python3-func_timeout -l pl.UTF-8
Moduł Pythona pozwalający na określenie limitów czasu przy wywoływaniu
dowolnej istniejącej funkcji. Obsługuje także zatrzymywanie wątków.

%package apidocs
Summary:	API documentation for Python func_timeout module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona func_timeout
Group:		Documentation

%description apidocs
API documentation for Python func_timeout module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona func_timeout.

%prep
%setup -q -n func_timeout-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} testit.py
#%{__python} tests/runTests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} testit.py
#%{__python3} tests/runTests.py
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

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/func_timeout/py2_raise.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%{py_sitescriptdir}/func_timeout
%{py_sitescriptdir}/func_timeout-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-func_timeout
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md
%{py3_sitescriptdir}/func_timeout
%{py3_sitescriptdir}/func_timeout-%{version}-py*.egg-info
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/*.html
