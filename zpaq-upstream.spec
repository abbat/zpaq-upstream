Name:          zpaq-upstream
Version:       6.60
Release:       1
Summary:       Maximum reference compressor for ZPAQ open standard
Group:         Productivity/Archiving/Compression
License:       GPL-3
URL:           https://github.com/abbat/zpaq-upstream
Conflicts:     zpaq
BuildRequires: gcc-c++, perl

Source0:       https://build.opensuse.org/source/home:antonbatenev:zpaq-upstream/zpaq-upstream/zpaq-upstream_%{version}.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}-build


%description
PAQ familily is a series of open source data compression archivers
that have evolved through collaborative development to top rankings
on several benchmarks measuring compression ratio although at the
expense of speed and memory usage.
.
This package includes ZPAQ, a proposed standard format for highly
compressed data that allows new compression algorithms to be
developed without breaking compatibility with older programs.


%prep
%setup -q -n zpaq-upstream


%build
g++ -O3 -Dunix -DNDEBUG src/zpaq.cpp src/libzpaq.cpp -pthread -o zpaq-upstream
/usr/bin/pod2man src/zpaq.pod > zpaq.1


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 zpaq-upstream %{buildroot}%{_bindir}/zpaq-upstream
install -m644 zpaq.1        %{buildroot}%{_mandir}/man1/zpaq.1

ln -s %{_bindir}/zpaq-upstream %{buildroot}%{_bindir}/zpaq


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/readme.txt
%doc %{_mandir}/man1/zpaq.1%{?ext_man}
%{_bindir}/zpaq
%{_bindir}/zpaq-upstream


%changelog
* Sat Dec 20 2014 Anton Batenev <antonbatenev@yandex.ru> 6.60-1
- Initial RPM release
