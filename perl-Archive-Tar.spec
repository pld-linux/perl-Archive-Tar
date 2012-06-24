#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Archive
%define		pnam	Tar
Summary:	Archive::Tar - a module for Perl manipulation of .tar files
Summary(cs):	Archive::Tar - modul pro zpracov�n� soubor� .tar v Perlu
Summary(da):	Archive::Tar - et modul for Perlh�ndtering af .tar-filer
Summary(de):	Archive::Tar - ein Modul f�r das Bearbeiten von .tar-Dateien durch Perl
Summary(es):	Archive::Tar - m�dulo para manipulaciones de Perl de los ficheros tar
Summary(fr):	Archive::Tar - module pour la manipulation Perl des fichiers .tar
Summary(it):	Archive::Tar - modulo per la gestione dei file .tar con Perl
Summary(ja):	Archive::Tar tar�ե������Perl���ΰ٤Υ⥸�塼��Ǥ���
Summary(ko):	Archive::Tar .tar ������ �����ϴ� Perl ���
Summary(pl):	Archive::Tar - modu� Perla do manipulacji plikami .tar
Summary(pt):	Archive::Tar - um m�dulo para a manipula��o em Perl dos ficheiros .tar
Summary(pt_BR):	Archive::Tar - um m�dulo para a manipula��o em Perl dos ficheiros .tar
Summary(sv):	Archive::Tar - en modul f�r Perlhantering av .tar-filer
Summary(tr):	Archive::Tar - .tar dosyalar� i�in bir Perl mod�l�
Summary(zh_CN):	Archive::Tar �� .tar �ļ����� Perl ������ģ�顣
Summary(zh_TW):	Archive::Tar �Ω� Perl �B�z .tar �ɮת��@�ӼҲաC
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
Toto je modul pro zpracov�n� archiv� tar. Archive::Tar poskytuje
objektov� orientovan� mechanismus pro zpracov�n� soubor� tar.
Poskytuje metody t��dy pro rychl� a snadn� zpracov�n� souboru a
umo��uje vytvo�en� objekt� soubor� tar pro vlastn� zpracov�n�. M�te-li
nainstalov�n modul Compress::Zlib, bude Archive::Tar tak� podporovat
soubory tar komprimovan� programem compress nebo gzip.

%description -l da
Dette er et modul for h�ndteringen af tar-arkiver. Archive::Tar
leverer en objektorienteret mekanisme til at h�ndtere tar-filer. Den
leverer klassemetoder for hurtig og nem filh�ndtering samtidigt med at
den muligg�r oprettelsen af tar-filobjekter for specialh�ndtering.
Hvis du har modulet Compress::Zlib installeret, vil Archive::Tar ogs�
underst�tte komprimerede eller gzip'ede tar-filer.

%description -l de
Dieses Modul dient der Bearbeitung von tar-Archiven. Archive::Tar
bietet einen objektspezifischen Mechanismus f�r das Bearbeiten von
solchen Archiven sowie Klassenmethoden f�r das schnelle und einfache
Bearbeiten und erm�glicht gleichzeitig das Anlegen von
tar-Dateiobjekten f�r das benutzerdefinierte Bearbeiten. Wenn Sie
bereits das Modul Compress::Zlib installiert haben, unterst�tzt
Archive::Tar auch komprimierte oder gzipped tar-Dateien.

%description -l es
Este m�dulo gestiona los ficheros tar. Archive::Tar proporciona un
mecanismo orientado a un objeto para gestionar ficheros tar.
Proporciona m�todos de clase para ficheros r�pidos y sencillos
mientras que permite la creaci�n de objetos de ficheros tar para la
manipulaci�n personalizada. Si tiene instalado el m�dulo
Compress::Zlib, Archive::Tar soportar� los ficheros tar comprimidos.

%description -l fr
Il s'agit d'un module de gestion des archives tar. Archive::Tar
fournit un m�canisme orient� sur l'objet pour la gestion des fichiers
tar. Il offre des m�thodes de classe permettant de g�rer rapidement et
facilement les fichiers tout en permettant de cr�er des objets de
fichiers tar pour une manipulation personnalis�e. Si vous avez
install� le module Compress::Zlib, Archive::Tar rendra �galement en
charge les fichiers tar comprim�s ou zipp�s.

%description -l it
Si tratta di un modulo per la gestione degli archivi tar. Archive::Tar
offre un meccanismo orientato agli oggetti per gestire i file tar.
Consente inoltre di gestire rapidamente e facilmente i file e di
creare gli oggetti dei file tar per la personalizzazione. Se il modulo
Compress::Zlib � installato, Archive::Tar supporter� anche i file tar
compressi o gzippati.

%description -l ko
�� ����� tar ��ī�̺� ������ ó���ϴµ� ���˴ϴ�. Archive::Tar��
tar ���� ó���� ���Ǵ� ��ü ������ ��Ŀ������ �����մϴ�. �� �����
������ ���� ���� ó���� ���� Ŭ���� ����� ������ �Ӹ� �ƴ϶� ����
����� ���� ������ ������ tar ���� ��ü�� ���� �����մϴ�.
Compress::Zlib ����� ��ġ�ϼ̴ٸ�, Archive::Tar�� ���� tar �����̳�
gzip ����� tar ���ϵ� �����մϴ�.

%description -l pl
Ten modu� obs�uguje archiwa tar. Archive::Tar udost�pnia zorientowany
obiektowo mechanizm obs�ugi plik�w tar. Udost�pnia klas� zawieraj�c�
metody umo�liwiaj�ce �atwe pos�ugiwanie sie plikami .tar, a tak�e
tworzenie obiekt�w tar i manipulacj� nimi. Je�li jest zainstalowany
modu� Compress::Zlib, Archive::Tar b�dzie obs�ugiwa� r�wnie� archiwa
tar spakowane dodatkowo programem compress lub gzip.

%description -l pt
Este � um m�dulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os m�todos das classes para o tratamento r�pido
e simples dos ficheiros enquanto permite tamb�m a cria��o de objectos
de ficheiros TAR para a manipula��o personalizada. Se tiver o m�dulo
Compress::Zlib instalado, o Archive::Tar ir� tamb�m suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l pt_BR
Este � um m�dulo para o tratamento dos pacotes TAR. O Archive::Tar
oferece um mecanismo orientado por objectos para lidar com os
ficheiros TAR. Oferece os m�todos das classes para o tratamento r�pido
e simples dos ficheiros enquanto permite tamb�m a cria��o de objectos
de ficheiros TAR para a manipula��o personalizada. Se tiver o m�dulo
Compress::Zlib instalado, o Archive::Tar ir� tamb�m suportar os
ficheiros TAR 'gzippados' ou 'compress'ed.

%description -l sv
Detta �r en modul f�r hanteringen av tar-arkiv. Archive::Tar
tillhandah�ller en objektorienterad mekanism f�r att hantera
tar-filer. Den tillhandah�ller klassmetoder f�r snabb och enkel
filhantering samtidigt som den m�jligg�r skapandet av tar-filobjekt
f�r specialhantering. Om du har modulen Compress::Zlib installerad,
kommer Archive::Tar ocks� att st�dja komprimerade eller gzip:ade
tar-filer.

%description -l zh_CN
������������ tar �鵵��ģ�顣Archive::Tar
�ṩ�˴��� tar �ļ����������Ļ��ơ����ṩ
����𷽷������ټ��׵ش����ļ�����������Ϊ
���ƵĲ��������� tar �ļ������������װ��
Compress::Zlib ģ�飬Archive::Tar ����֧��ѹ
���Ļ��� gzip ����� tar �ļ���

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
