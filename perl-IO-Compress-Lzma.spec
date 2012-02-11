#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Compress-Lzma
%include	/usr/lib/rpm/macros.perl
Summary:	IO::Compress::Lzma - Perl interface to read/write lzma files/buffers
Summary(pl.UTF-8):	IO::Compress::Lzma - perlowy interfejs do odczytu/zapisu buforów/plików lzma
Name:		perl-IO-Compress-Lzma
Version:	2.048
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/PMQS/IO-Compress-Lzma-%{version}.tar.gz
# Source0-md5:	f21d77a1530d6e8ecd28f732d26c8329
URL:		http://search.cpan.org/dist/IO-Compress-Lzma/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-Raw-Lzma >= %{version}
BuildRequires:	perl-IO-Compress >= %{version}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to allow reading and writing of
lzma files/buffers.

%description -l pl.UTF-8
Ten moduł udostępnia perlowy interfejs pozwalający na odczyt i zapis
plików/buforów lzma.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Compress/Lzma.pm
%{perl_vendorlib}/IO/Compress/Xz.pm
%{perl_vendorlib}/IO/Compress/Adapter/Lzma.pm
%{perl_vendorlib}/IO/Compress/Adapter/Xz.pm
%{perl_vendorlib}/IO/Uncompress/UnLzma.pm
%{perl_vendorlib}/IO/Uncompress/UnXz.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/UnLzma.pm
%{perl_vendorlib}/IO/Uncompress/Adapter/UnXz.pm
%{_mandir}/man3/IO::Compress::Lzma.3pm*
%{_mandir}/man3/IO::Compress::Xz.3pm*
%{_mandir}/man3/IO::Uncompress::UnLzma.3pm*
%{_mandir}/man3/IO::Uncompress::UnXz.3pm*
%{_examplesdir}/%{name}-%{version}
