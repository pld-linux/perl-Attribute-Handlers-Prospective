#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Attribute
%define		pnam	Handlers-Prospective
Summary:	Attribute::Handlers::Prospective - Enhanced definition of attribute handlers
Summary(pl):	Attribute::Handlers::Prospective - rozszerzona definicja obs�ugi atrybut�w
Name:		perl-Attribute-Handlers-Prospective
Version:	0.01
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Filter-Simple
BuildRequires:	perl-Parse-RecDescent
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module, when inherited by a package, allows that package's class
to define attribute handler subroutines for specific attributes.
Variables and subroutines subsequently defined in that package, or in
packages derived from that package may be given attributes with the
same names as the attribute handler subroutines, which will then be
called at the end of the compilation phase (i.e. in an INIT block).

%description -l pl
Ten modu�, w przypadku dziedziczenia po nim w pakiecie, pozwala klasie
pakietu definiowa� funkcje obs�ugi atrybut�w dla danych atrybut�w.
Zmienne i funkcje zdefiniowane w tym pakiecie lub pakietach
wywodz�cych si� z niego mog� mie� podane atrybuty o tych samych
nazwach co funkcje obs�uguj�ce atrybuty, kt�re b�d� wtedy wywo�ywane
na ko�cu fazy kompilacji (czyli w bloku INIT).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%dir %{perl_sitelib}/Attribute/Handlers
%{perl_sitelib}/Attribute/Handlers/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
