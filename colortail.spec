Summary:	Colored "tail"
Summary(pl):	Kolorowy "tail"
Name:		colortail
Version:	0.3.0
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://www.student.hk-r.se/~pt98jan/%{name}-%{version}.tar.gz
# Source0-md5:	2589d3e372080f4052d1cc0d6550508f
Patch0:		%{name}-headers.patch
URL:		http://www.student.hk-r.se/~pt98jan/colortail.html
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Colortail works like tail but can optionally read a color config file,
where it's specified which patterns result in which colors.

%description -l pl
Colortail dzia³a na podobne zasadzie jak zwyk³y tail, z t± ró¿nic±, ¿e
potrafi wy¶wietlaæ kolorowy tekst w zale¿no¶ci od ustawieñ w pliku
konfiguracyjnym.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-ext_regex
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install example-conf/conf.* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not mtime size md5)  %{_sysconfdir}/%{name}/*
