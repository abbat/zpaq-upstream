Name:          zpaq-6.55
Version:       6.55
Release:       2
Summary:       Maximum reference compressor for ZPAQ open standard
Group:         Productivity/Archiving/Compression
License:       GPL-3
URL:           https://github.com/abbat/zpaq-upstream/tree/v6.55
Conflicts:     zpaq, zpaq-upstream
BuildRequires: gcc-c++, binutils

Source0:       https://build.opensuse.org/source/home:antonbatenev:zpaq-upstream/%{name}/%{name}_%{version}.tar.bz2
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


%define debug_package %{nil}


%prep
%setup -q -n %{name}


%build
g++ -O3 -Dunix -DNDEBUG src/zpaq.cpp src/libzpaq.cpp src/divsufsort.c -pthread -o %{name}


%install
install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}/%{name}
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/zpaq


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/readme.txt
%{_bindir}/zpaq
%{_bindir}/%{name}


%changelog
* Wed May 13 2015 Anton Batenev <antonbatenev@yandex.ru> 6.55-1
- Initial RPM release
