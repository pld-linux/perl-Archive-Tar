%include	/usr/lib/rpm/macros.perl
Summary:	Archive-Tar perl module
Summary(pl):	Modu³ perla Archive-Tar
Name:		perl-Archive-Tar
Version:	0.07
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Archive/Tar-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Archive-Tar - module for manipulation of tar archives.

%description -l pl
Archive-Tar - modu³ do manipulacji archiwami tar.

%prep
%setup -q -n Tar-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install ptar $RPM_BUILD_ROOT%{_bindir}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Archive/Tar
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz
%attr(755,root,root) %{_bindir}/ptar
%{perl_sitelib}/Archive/Tar.pm
%{perl_sitearch}/auto/Archive/Tar

%{_mandir}/man3/*
