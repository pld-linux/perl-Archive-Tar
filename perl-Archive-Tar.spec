%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Tar
Summary:	Archive::Tar Perl module
Summary(cs):	Modul Archive::Tar pro Perl
Summary(da):	Perlmodul Archive::Tar
Summary(de):	Archive::Tar Perl Modul
Summary(es):	Módulo de Perl Archive::Tar
Summary(fr):	Module Perl Archive::Tar
Summary(it):	Modulo di Perl Archive::Tar
Summary(ja):	Archive::Tar Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Archive::Tar ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Archive::Tar
Summary(pl):	Modu³ Perla Archive::Tar
Summary(pt):	Módulo de Perl Archive::Tar
Summary(pt_BR):	Módulo Perl Archive::Tar
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Archive::Tar
Summary(sv):	Archive::Tar Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Archive::Tar
Summary(zh_CN):	Archive::Tar Perl Ä£¿é
Name:		perl-Archive-Tar
Version:	0.22
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive::Tar - module for manipulation of tar archives.

%description -l pl
Archive::Tar - modu³ do manipulacji archiwami tar.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install ptar $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/ptar
%{perl_sitelib}/Archive/Tar.pm
%{_mandir}/man3/*
