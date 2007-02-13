#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Attribute
%define		pnam	Handlers-Prospective
Summary:	Attribute::Handlers::Prospective - enhanced definition of attribute handlers
Summary(pl.UTF-8):	Attribute::Handlers::Prospective - rozszerzona definicja obsługi atrybutów
Name:		perl-Attribute-Handlers-Prospective
Version:	0.01
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d20442ca3d7f83aacbdb15f225fdf287
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Filter-Simple
BuildRequires:	perl-Parse-RecDescent
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module, when inherited by a package, allows that package's class
to define attribute handler subroutines for specific attributes.
Variables and subroutines subsequently defined in that package, or in
packages derived from that package may be given attributes with the
same names as the attribute handler subroutines, which will then be
called at the end of the compilation phase (i.e. in an INIT block).

%description -l pl.UTF-8
Ten moduł, w przypadku dziedziczenia po nim w pakiecie, pozwala klasie
pakietu definiować funkcje obsługi atrybutów dla danych atrybutów.
Zmienne i funkcje zdefiniowane w tym pakiecie lub pakietach
wywodzących się z niego mogą mieć podane atrybuty o tych samych
nazwach co funkcje obsługujące atrybuty, które będą wtedy wywoływane
na końcu fazy kompilacji (czyli w bloku INIT).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_vendorlib}/Attribute/Handlers
%{perl_vendorlib}/Attribute/Handlers/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
