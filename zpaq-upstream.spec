Name:          zpaq-upstream
Version:       7.15
Release:       1
Summary:       Maximum reference compressor for ZPAQ open standard
Group:         Productivity/Archiving/Compression
License:       Public Domain
URL:           https://github.com/abbat/zpaq-upstream
Conflicts:     zpaq, zpaq-6.55
BuildRequires: gcc-c++, perl, binutils

%if 0%{?fedora} >= 19
BuildRequires: perl-podlators
%endif

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
%setup -q -n zpaq-upstream


%build
g++ -O3 -Dunix -DNDEBUG src/zpaq.cpp src/libzpaq.cpp -pthread -o %{name}
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
%doc src/readme.txt src/COPYING
%doc %{_mandir}/man1/zpaq.1*
%{_bindir}/zpaq
%{_bindir}/zpaq-upstream


%changelog
* Wed Sep 14 2016 Anton Batenev <antonbatenev@yandex.ru> 7.15-1
- Initial RPM release
