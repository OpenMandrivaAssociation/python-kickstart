%define srcname pykickstart

Name:		python-kickstart
Version:	3.18
Release:	2
License:	GPLv2 and MIT
Group:		Development/Python
Summary:	Python library and tools for manipulating kickstart files
URL:		http://fedoraproject.org/wiki/pykickstart
# This is a Red Hat maintained package. Thus the source is only available from
# within the srpm:
# https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/SRPMS/Packages/p/
# or git: git://github.com/rhinstaller/pykickstart.git
Source0:	%{srcname}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	gettext

BuildRequires:	python-devel
BuildRequires:	python-ordered-set
BuildRequires:	python-setuptools
BuildRequires:	python-requests
BuildRequires:	python-six
Requires: 	python-six
Requires: 	python-requests
Requires: 	python-ordered-set
# Proper package name for this module
Provides:	python-pykickstart = %{version}-%{release}
# Fedora package name for utilities
Provides:	pykickstart = %{version}-%{release}
# Mageia package name for utilities
Provides:	python-kickstart-utils = %{version}-%{release}
# Mageia package name for Python module
Provides:	python3-kickstart = %{version}-%{release}
# Fedora package name for Python module
Provides:	python3-pykickstart = %{version}-%{release}

%description
Python library and tools for manipulating kickstart files.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
make PYTHON=%{__python3}


%install
%make_install PYTHON=%{__python3}


%files
%license COPYING
%doc README.rst
%doc data/kickstart.vim
%doc docs/2to3
%doc docs/programmers-guide
%doc docs/kickstart-docs.txt
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
%{_bindir}/ksshell
%{_mandir}/man1/*
%{python3_sitelib}/pykickstart/
%{python3_sitelib}/pykickstart*.egg-info

