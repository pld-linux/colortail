Summary:	Colored "tail"
Summary(pl):	Kolorowy "Tail"
Name:		colortail
Version:	0.2.0
Release:	2
Source:		%{name}-%{version}.tar.gz
URL:		http://www.student.hk-r.se/~pt98jan/colortail.html
Copyright:	GNU
Group:		System/utilities
Packager:	Andrzej Nakonieczny <dzemik@ps.pl>
BuildRoot:	/tmp/%{name}-%{version}-%{release}-buildroot

%description
Colortail works like tail but can optionally read a color config file. Where
it's specified which patterns result in which colors.

%description -l pl
Colortail dzia³a na podobne zasadzie jak zwyk³y tail, z t± ró¿nic±, ¿e potrafi 
wy¶wietlaæ kolorowy tekst w zale¿no¶ci od ustwieñ w pliku konfiguracyjnym.

%prep
%setup -q

%build

./configure --enable-ext_regex

make CFLAGS="$RPM_OPT_FLAGS" LDCONFIG="-s"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p 	$RPM_BUILD_ROOT/usr/{bin,man/man1}
mkdir -p 	$RPM_BUILD_ROOT/etc

install colortail	$RPM_BUILD_ROOT/usr/bin
install colortail.1	$RPM_BUILD_ROOT/usr/man/man1
install CONFIG		$RPM_BUILD_ROOT/etc/colortail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (644, root, root, 755)
%doc README ChangeLog README TODO
%attr (755, root, root) /usr/bin/*
%attr (644, root, root) /usr/man/man1/*
%attr (644, root, root) /etc/*

%changelog

* Wed Jul  7 1999 Andrzej Nakonieczny <dzemik@ps.pl>
  [0.2.0-2]
- fixed perminnsion on directories.

* Sat May 08 1999 Andrzej Nakonieczny <dzemik@ps.pl>
  [0.2.0-1]
- First release of this package.
