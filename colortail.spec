Summary:	Colored "tail"
Summary(pl):	Kolorowy "tail"
Name:		colortail
Version:	0.3.0
Release:	1
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt98jan/colortail.html
Copyright:	GNU
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
Colortail works like tail but can optionally read a color config file,
where it's specified which patterns result in which colors.

%description -l pl
Colortail dzia³a na podobne zasadzie jak zwyk³y tail, z t± ró¿nic±, ¿e
potrafi wy¶wietlaæ kolorowy tekst w zale¿no¶ci od ustwieñ w pliku
konfiguracyjnym.

%prep
%setup -q
%build

aclocal
autoconf
automake -a -c
autoheader
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-ext_regex
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install example-conf/conf.* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

gzip -9nf ChangeLog README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not mtime size md5)  %{_sysconfdir}/%{name}/*
