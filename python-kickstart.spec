%define srcname pykickstart

Name:		python-kickstart
Version:	1.68
Release:	%mkrel 1
Summary:	A python library for manipulating kickstart files
License:	GPLv2
Group:		Development/Python
# This is a Red Hat maintained package. Thus the source is only available from
# within the srpm:
# http://download.fedora.redhat.com/pub/fedora/linux/development/source/SRPMS/
# or git git://git.fedorahosted.org/git/pykickstart.git
Source0:	%{srcname}-%{version}.tar.gz
Url:		http://fedoraproject.org/wiki/pykickstart
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	gettext
BuildArch:	noarch
Requires:	python-urlgrabber

%description
The python-kickstart package is a python library for manipulating kickstart files.

%prep
%setup -q -n %{srcname}-%{version}

%build
%make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{srcname}

%clean
rm -rf %{buildroot}

%files -f %{srcname}.lang
%defattr(-,root,root,-)
%doc README ChangeLog COPYING docs/programmers-guide
%doc docs/kickstart-docs.txt
%{python_sitelib}/*
%{_bindir}/ksvalidator
%{_bindir}/ksflatten
%{_bindir}/ksverdiff
