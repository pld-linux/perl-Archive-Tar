%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Archive-Tar perl module
Summary(pl):	Modu³ perla Archive-Tar
Name:		perl-Archive-Tar
Version:	0.07
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Archive/Tar-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Archive-Tar - module for manipulation of tar archives. 

%description -l pl
Archive-Tar - modu³ do manipulacji archiwami tar.

%prep
%setup -q -n Tar-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

make install DESTDIR=$RPM_BUILD_ROOT

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
