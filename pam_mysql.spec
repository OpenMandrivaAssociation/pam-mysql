%define name	pam_mysql
%define url	http://sourceforge.net/projects/pam-mysql/
%define version 0.5
%define prefix	%{_prefix}
%define release %mkrel 6

Summary:	MySQL authentication for PAM
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://sourceforge.net/projects/pam-mysql/
Source:		%{url}/pam_mysql-%{version}.tar.bz2
Requires:	pam
BuildRequires:	pam-devel, MySQL-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a module that allows people to login to PAM-aware applications by
authenticating to a MySQL database. Now configurable in terms of which host the
database resides upon and which table and username and password column to
interrogate.

%prep

%setup -q -n %{name}

%build

%make

%install
mkdir -p $RPM_BUILD_ROOT/lib/security
cp pam_mysql.so $RPM_BUILD_ROOT/lib/security
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
cp Changelog $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
cp CREDITS $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
cp Readme $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%doc Changelog CREDITS Readme
/lib/security/pam_mysql.so

