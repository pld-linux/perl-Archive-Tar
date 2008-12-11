#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Tar
Summary:	Archive::Tar - a module for Perl manipulation of .tar files
Summary(cs.UTF-8):	Archive::Tar - modul pro zpracování souborů .tar v Perlu
Summary(da.UTF-8):	Archive::Tar - et modul for Perlhåndtering af .tar-filer
Summary(de.UTF-8):	Archive::Tar - ein Modul für das Bearbeiten von .tar-Dateien durch Perl
Summary(es.UTF-8):	Archive::Tar - módulo para manipulaciones de Perl de los ficheros tar
Summary(fr.UTF-8):	Archive::Tar - module pour la manipulation Perl des fichiers .tar
Summary(it.UTF-8):	Archive::Tar - modulo per la gestione dei file .tar con Perl
Summary(ja.UTF-8):	Archive::Tar tarファイルのPerl操作の為のモジュールです。
Summary(ko.UTF-8):	Archive::Tar .tar 파일을 조작하는 Perl 모듈
Summary(pl.UTF-8):	Archive::Tar - moduł Perla do manipulacji plikami .tar
Summary(pt.UTF-8):	Archive::Tar - um módulo para a manipulação em Perl dos ficheiros .tar
Summary(pt_BR.UTF-8):	Archive::Tar - um módulo para a manipulação em Perl dos ficheiros .tar
Summary(sv.UTF-8):	Archive::Tar - en modul för Perlhantering av .tar-filer
Summary(tr.UTF-8):	Archive::Tar - .tar dosyaları için bir Perl modülü
Summary(zh_CN.UTF-8):	Archive::Tar 对 .tar 文件进行 Perl 操作的模块。
Summary(zh_TW.UTF-8):	Archive::Tar 用於 Perl 處理 .tar 檔案的一個模組。
Name:		perl-Archive-Tar
Version:	1.40
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Archive/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df0322a37c5282a12da636c6f48d25e4
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

%description -l cs.UTF-8
Toto je modul pro zpracování archivů tar. Archive::Tar poskytuje
objektově orientovaný mechanismus pro zpracování souborů tar.
Poskytuje metody třídy pro rychlé a snadné zpracování souboru a
umožňuje vytvoření objektů souborů tar pro vlastní zpracování. Máte-li
nainstalován modul Compress::Zlib, bude Archive::Tar také podporovat
soubory tar komprimované programem compress nebo gzip.

%description -l da.UTF-8
Dette er et modul for håndteringen af tar-arkiver. Archive::Tar
leverer en objektorienteret mekanisme til at håndtere tar-filer. Den
leverer klassemetoder for hurtig og nem filhåndtering samtidigt med at
den muliggør oprettelsen af tar-filobjekter for specialhåndtering.
Hvis du har modulet Compress::Zlib installeret, vil Archive::Tar også
understøtte komprimerede eller gzip'ede tar-filer.

%description -l de.UTF-8
Dieses Modul dient der Bearbeitung von tar-Archiven. Archive::Tar
bietet einen objektspezifischen Mechanismus für das Bearbeiten von
solchen Archiven sowie Klassenmethoden für das schnelle und einfache
Bearbeiten und ermöglicht gleichzeitig das Anlegen von
tar-Dateiobjekten für das benutzerdefinierte Bearbeiten. Wenn Sie
bereits das Modul Compress::Zlib installiert haben, unterstützt
Archive::Tar auch komprimierte oder gzipped tar-Dateien.

%description -l es.UTF-8
Este módulo gestiona los ficheros tar. Archive::Tar proporciona un
mecanismo orientado a un objeto para gestionar ficheros tar.
Proporciona métodos de clase para ficheros rápidos y sencillos
mientras que permite la creación de objetos de ficheros tar para la
manipulación personalizada. Si tiene instalado el módulo
Compress::Zlib, Archive::Tar soportará los ficheros tar comprimidos.

%description -l fr.UTF-8
Il s'agit d'un module de gestion des archives tar. Archive::Tar
fournit un mécanisme orienté sur l'objet pour la gestion des fichiers
tar. Il offre des méthodes de classe permettant de gérer rapidement et
facilement les fichiers tout en permettant de créer des objets de
fichiers tar pour une manipulation personnalisée. Si vous avez
installé le module Compress::Zlib, Archive::Tar rendra également en
charge les fichiers tar comprimés ou zippés.

%description -l it.UTF-8
Si tratta di un modulo per la gestione degli archivi tar. Archive::Tar
offre un meccanismo orientato agli oggetti per gestire i file tar.
Consente inoltre di gestire rapidamente e facilmente i file e di
creare gli oggetti dei file tar per la personalizzazione. Se il modulo
Compress::Zlib è installato, Archive::Tar supporterà anche i file tar
compressi o gzippati.

%description -l ko.UTF-8
이 모듈은 tar 아카이브 파일을 처리하는데 사용됩니다. Archive::Tar는
tar 파일 처리에 사용되는 객체 지향적 메커니즘을 제공합니다. 이 모듈은
빠르고 쉬운 파일 처리를 위한 클래스 방식을 제공할 뿐만 아니라 또한
사용자 설정 조작이 가능한 tar 파일 객체도 생성 가능합니다.
Compress::Zlib 모듈을 설치하셨다면, Archive::Tar는 압축 tar 파일이나
gzip 압축된 tar 파일도 지원합니다.

%description -l pl.UTF-8
Ten moduł obsługuje archiwa tar. Archive::Tar udostępnia zorientowany
obiektowo mechanizm obsługi plików tar. Udostępnia klasę zawierającą
metody umożliwiające łatwe posługiwanie sie plikami .tar, a także
tworzenie obiektów tar i manipulację nimi. Jeśli jest zainstalowany
moduł Compress::Zlib, Archive::Tar będzie obsługiwać również archiwa
tar spakowane dodatkowo programem compress lub gzip.

%description -l pt.UTF-8
Este é um módulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os métodos das classes para o tratamento rápido
e simples dos ficheiros enquanto permite também a criação de objectos
de ficheiros TAR para a manipulação personalizada. Se tiver o módulo
Compress::Zlib instalado, o Archive::Tar irá também suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l pt_BR.UTF-8
Este é um módulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os métodos das classes para o tratamento rápido
e simples dos ficheiros enquanto permite também a criação de objectos
de ficheiros TAR para a manipulação personalizada. Se tiver o módulo
Compress::Zlib instalado, o Archive::Tar irá também suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l sv.UTF-8
Detta är en modul för hanteringen av tar-arkiv. Archive::Tar
tillhandahåller en objektorienterad mekanism för att hantera
tar-filer. Den tillhandahåller klassmetoder för snabb och enkel
filhantering samtidigt som den möjliggör skapandet av tar-filobjekt
för specialhantering. Om du har modulen Compress::Zlib installerad,
kommer Archive::Tar också att stödja komprimerade eller gzip:ade
tar-filer.

%description -l zh_CN.UTF-8
这是用来处理 tar 归档的模块。Archive::Tar
提供了处理 tar 文件的面向对象的机制。它提供
了类别方法来快速简易地处理文件，它还允许为
定制的操作而创建 tar 文件对象。如果您安装了
Compress::Zlib 模块，Archive::Tar 还会支持压
缩的或用 gzip 处理的 tar 文件。

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
