#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Tar
Summary:	Archive::Tar - a module for Perl manipulation of .tar files
Summary(cs):	Archive::Tar - modul pro zpracování souborù .tar v Perlu
Summary(da):	Archive::Tar - et modul for Perlhåndtering af .tar-filer
Summary(de):	Archive::Tar - ein Modul für das Bearbeiten von .tar-Dateien durch Perl
Summary(es):	Archive::Tar - módulo para manipulaciones de Perl de los ficheros tar
Summary(fr):	Archive::Tar - module pour la manipulation Perl des fichiers .tar
Summary(it):	Archive::Tar - modulo per la gestione dei file .tar con Perl
Summary(ja):	Archive::Tar tar¥Õ¥¡¥¤¥ë¤ÎPerlÁàºî¤Î°Ù¤Î¥â¥¸¥å¡¼¥ë¤Ç¤¹¡£
Summary(ko):	Archive::Tar .tar ÆÄÀÏÀ» Á¶ÀÛÇÏ´Â Perl ¸ğµâ
Summary(pl):	Archive::Tar - modu³ Perla do manipulacji plikami .tar
Summary(pt):	Archive::Tar - um módulo para a manipulação em Perl dos ficheiros .tar
Summary(pt_BR):	Archive::Tar - um módulo para a manipulação em Perl dos ficheiros .tar
Summary(sv):	Archive::Tar - en modul för Perlhantering av .tar-filer
Summary(tr):	Archive::Tar - .tar dosyaları için bir Perl modülü
Summary(zh_CN):	Archive::Tar ¶Ô .tar ÎÄ¼ş½øĞĞ Perl ²Ù×÷µÄÄ£¿é¡£
Summary(zh_TW):	Archive::Tar ¥Î©ó Perl ³B²z .tar ÀÉ®×ªº¤@­Ó¼Ò²Õ¡C
Name:		perl-Archive-Tar
Version:	1.30
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	89604ea8fadc990c7bb668259dacb439
URL:		http://search.cpan.org/dist/Archive-Tar/
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-IO-Zlib >= 1.01
BuildRequires:	perl-Test-Harness >= 2.26
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-IO-Zlib >= 1.01
Requires:	perl-Text-Diff
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a module for the handling of tar archives. Archive::Tar
provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy file handling while also
allowing for the creation of tar file objects for custom manipulation.
If you have the Compress::Zlib module installed, Archive::Tar will
also support compressed or gzipped tar files.

%description -l cs
Toto je modul pro zpracování archivù tar. Archive::Tar poskytuje
objektovì orientovanı mechanismus pro zpracování souborù tar.
Poskytuje metody tøídy pro rychlé a snadné zpracování souboru a
umo¾òuje vytvoøení objektù souborù tar pro vlastní zpracování. Máte-li
nainstalován modul Compress::Zlib, bude Archive::Tar také podporovat
soubory tar komprimované programem compress nebo gzip.

%description -l da
Dette er et modul for håndteringen af tar-arkiver. Archive::Tar
leverer en objektorienteret mekanisme til at håndtere tar-filer. Den
leverer klassemetoder for hurtig og nem filhåndtering samtidigt med at
den muliggør oprettelsen af tar-filobjekter for specialhåndtering.
Hvis du har modulet Compress::Zlib installeret, vil Archive::Tar også
understøtte komprimerede eller gzip'ede tar-filer.

%description -l de
Dieses Modul dient der Bearbeitung von tar-Archiven. Archive::Tar
bietet einen objektspezifischen Mechanismus für das Bearbeiten von
solchen Archiven sowie Klassenmethoden für das schnelle und einfache
Bearbeiten und ermöglicht gleichzeitig das Anlegen von
tar-Dateiobjekten für das benutzerdefinierte Bearbeiten. Wenn Sie
bereits das Modul Compress::Zlib installiert haben, unterstützt
Archive::Tar auch komprimierte oder gzipped tar-Dateien.

%description -l es
Este módulo gestiona los ficheros tar. Archive::Tar proporciona un
mecanismo orientado a un objeto para gestionar ficheros tar.
Proporciona métodos de clase para ficheros rápidos y sencillos
mientras que permite la creación de objetos de ficheros tar para la
manipulación personalizada. Si tiene instalado el módulo
Compress::Zlib, Archive::Tar soportará los ficheros tar comprimidos.

%description -l fr
Il s'agit d'un module de gestion des archives tar. Archive::Tar
fournit un mécanisme orienté sur l'objet pour la gestion des fichiers
tar. Il offre des méthodes de classe permettant de gérer rapidement et
facilement les fichiers tout en permettant de créer des objets de
fichiers tar pour une manipulation personnalisée. Si vous avez
installé le module Compress::Zlib, Archive::Tar rendra également en
charge les fichiers tar comprimés ou zippés.

%description -l it
Si tratta di un modulo per la gestione degli archivi tar. Archive::Tar
offre un meccanismo orientato agli oggetti per gestire i file tar.
Consente inoltre di gestire rapidamente e facilmente i file e di
creare gli oggetti dei file tar per la personalizzazione. Se il modulo
Compress::Zlib è installato, Archive::Tar supporterà anche i file tar
compressi o gzippati.

%description -l ko
ÀÌ ¸ğµâÀº tar ¾ÆÄ«ÀÌºê ÆÄÀÏÀ» Ã³¸®ÇÏ´Âµ¥ »ç¿ëµË´Ï´Ù. Archive::Tar´Â
tar ÆÄÀÏ Ã³¸®¿¡ »ç¿ëµÇ´Â °´Ã¼ ÁöÇâÀû ¸ŞÄ¿´ÏÁòÀ» Á¦°øÇÕ´Ï´Ù. ÀÌ ¸ğµâÀº
ºü¸£°í ½¬¿î ÆÄÀÏ Ã³¸®¸¦ À§ÇÑ Å¬·¡½º ¹æ½ÄÀ» Á¦°øÇÒ »Ó¸¸ ¾Æ´Ï¶ó ¶ÇÇÑ
»ç¿ëÀÚ ¼³Á¤ Á¶ÀÛÀÌ °¡´ÉÇÑ tar ÆÄÀÏ °´Ã¼µµ »ı¼º °¡´ÉÇÕ´Ï´Ù.
Compress::Zlib ¸ğµâÀ» ¼³Ä¡ÇÏ¼Ì´Ù¸é, Archive::Tar´Â ¾ĞÃà tar ÆÄÀÏÀÌ³ª
gzip ¾ĞÃàµÈ tar ÆÄÀÏµµ Áö¿øÇÕ´Ï´Ù.

%description -l pl
Ten modu³ obs³uguje archiwa tar. Archive::Tar udostêpnia zorientowany
obiektowo mechanizm obs³ugi plików tar. Udostêpnia klasê zawieraj±c±
metody umo¿liwiaj±ce ³atwe pos³ugiwanie sie plikami .tar, a tak¿e
tworzenie obiektów tar i manipulacjê nimi. Je¶li jest zainstalowany
modu³ Compress::Zlib, Archive::Tar bêdzie obs³ugiwaæ równie¿ archiwa
tar spakowane dodatkowo programem compress lub gzip.

%description -l pt
Este é um módulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os métodos das classes para o tratamento rápido
e simples dos ficheiros enquanto permite também a criação de objectos
de ficheiros TAR para a manipulação personalizada. Se tiver o módulo
Compress::Zlib instalado, o Archive::Tar irá também suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l pt_BR
Este é um módulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os métodos das classes para o tratamento rápido
e simples dos ficheiros enquanto permite também a criação de objectos
de ficheiros TAR para a manipulação personalizada. Se tiver o módulo
Compress::Zlib instalado, o Archive::Tar irá também suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l sv
Detta är en modul för hanteringen av tar-arkiv. Archive::Tar
tillhandahåller en objektorienterad mekanism för att hantera
tar-filer. Den tillhandahåller klassmetoder för snabb och enkel
filhantering samtidigt som den möjliggör skapandet av tar-filobjekt
för specialhantering. Om du har modulen Compress::Zlib installerad,
kommer Archive::Tar också att stödja komprimerade eller gzip:ade
tar-filer.

%description -l zh_CN
ÕâÊÇÓÃÀ´´¦Àí tar ¹éµµµÄÄ£¿é¡£Archive::Tar
Ìá¹©ÁË´¦Àí tar ÎÄ¼şµÄÃæÏò¶ÔÏóµÄ»úÖÆ¡£ËüÌá¹©
ÁËÀà±ğ·½·¨À´¿ìËÙ¼òÒ×µØ´¦ÀíÎÄ¼ş£¬Ëü»¹ÔÊĞíÎª
¶¨ÖÆµÄ²Ù×÷¶ø´´½¨ tar ÎÄ¼ş¶ÔÏó¡£Èç¹ûÄú°²×°ÁË
Compress::Zlib Ä£¿é£¬Archive::Tar »¹»áÖ§³ÖÑ¹
ËõµÄ»òÓÃ gzip ´¦ÀíµÄ tar ÎÄ¼ş¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/ptar*
%{perl_vendorlib}/Archive/Tar.pm
%{perl_vendorlib}/Archive/Tar
%{_mandir}/man1/ptar*
%{_mandir}/man3/*
