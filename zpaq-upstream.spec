Name:          zpaq-upstream
Version:       6.59
Release:       1
Summary:       Maximum reference compressor for ZPAQ open standard
Group:         Productivity/Archiving/Compression
License:       GPL-3
URL:           https://github.com/abbat/zpaq-upstream
Conflicts:     zpaq
BuildRequires: gcc-c++

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


%install
install -d %{buildroot}%{_bindir}
install -m755 zpaq-upstream %{buildroot}%{_bindir}/zpaq-upstream
ln -s %{_bindir}/zpaq-upstream %{buildroot}%{_bindir}/zpaq


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc src/readme.txt src/zpaq.pod
%{_bindir}/zpaq
%{_bindir}/zpaq-upstream


%changelog
* Sat Dec 13 2014 Anton Batenev <antonbatenev@yandex.ru> 6.59-1
- Initial RPM release
