%include	/usr/lib/rpm/macros.perl
Summary:	Archive-Tar perl module
Summary(pl):	Modu³ perla Archive-Tar
Name:		perl-Archive-Tar
Version:	0.22
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Archive/Archive-Tar-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive-Tar - module for manipulation of tar archives.

%description -l pl
Archive-Tar - modu³ do manipulacji archiwami tar.

%prep
%setup -q -n Archive-Tar-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install ptar $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ptar
%{perl_sitelib}/Archive/Tar.pm
%{_mandir}/man3/*
