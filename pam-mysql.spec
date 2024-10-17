%define name	pam-mysql
%define url	http://sourceforge.net/projects/pam-mysql/
%define version 0.5
%define prefix	%{_prefix}
%define release 6mdk

Summary:	MySQL authentication for PAM
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		https://sourceforge.net/projects/pam-mysql/
Source0:	%{url}/pam_mysql-%{version}.tar.bz2
Requires:	pam
BuildRequires:	pam-devel, mysql-devel

%description
This is a module that allows people to login to PAM-aware applications by
authenticating to a MySQL database. Now configurable in terms of which host the
database resides upon and which table and username and password column to
interrogate.

%prep

%setup -q -n pam_mysql

%build

%make

%install
mkdir -p %{buildroot}/lib/security
cp pam_mysql.so %{buildroot}/lib/security
mkdir -p %{buildroot}/usr/share/doc/pam-mysql-%{version}

%files
/lib/security/pam_mysql.so
