Summary:	Colored "tail"
Summary(pl):	Kolorowy "Tail"
Name:		colortail
Version:	0.2.0
Release:	2
Source:		%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt98jan/colortail.html
Copyright:	GNU
Group:		System/utilities
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Colortail works like tail but can optionally read a color config file. Where
it's specified which patterns result in which colors.

%description -l pl
Colortail dzia³a na podobne zasadzie jak zwyk³y tail, z t± ró¿nic±, ¿e potrafi 
wy¶wietlaæ kolorowy tekst w zale¿no¶ci od ustwieñ w pliku konfiguracyjnym.

%prep
%setup -q

%build

LDFLAGS="-s"; export LDFLAGS
%configure --enable-ext_regex

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install colortail	$RPM_BUILD_ROOT%{_bindir}
install colortail.1	$RPM_BUILD_ROOT%{_mandir}/man1
install CONFIG		$RPM_BUILD_ROOT%{_sysconfdir}/colortail

gzip -9f $RPM_BUILD_ROOT%{_mandir}/man1/* \
	ChangeLog README TODO
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not mtime size md5)  %{_sysconfdir}/*
