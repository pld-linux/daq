Summary:	Data Acquisition Library
Name:		daq
Version:	2.0.6
Release:	1
License:	GNU General Public License
Group:		Networking
Source0:	https://www.snort.org/downloads/snort/%{name}-%{version}.tar.gz
# Source0-md5:	2cd6da422a72c129c685fc4bb848c24c
URL:		http://www.snort.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libdnet-devel
BuildRequires:	libnetfilter_queue-devel
BuildRequires:	libpcap-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data Acquisition library for Snort.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package static
Summary:	Static %{name} library
Summary(pl.UTF-8):	Statyczna biblioteka %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static %{name} library.

%description static -l pl.UTF-8
Statyczna biblioteka %{name}.

%prep
%setup -q

%build
%configure \
	--enable-ipv6

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
/sbin/ldconfig

%preun

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_libdir}/daq
%{_libdir}/daq/daq_*.so
%attr(755,root,root) %ghost %{_libdir}/libdaq.so.2
%attr(755,root,root) %{_libdir}/libdaq.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsfbpf.so.0
%attr(755,root,root) %{_libdir}/libsfbpf.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libdaq.so
%attr(755,root,root) %{_libdir}/libsfbpf.so
%{_libdir}/libdaq.la
%{_libdir}/libsfbpf.la
%attr(755,root,root) %{_bindir}/daq-modules-config

%files static
%defattr(644,root,root,755)
%{_libdir}/libdaq.a
%{_libdir}/libdaq_static.a
%{_libdir}/libdaq_static_modules.a
%{_libdir}/libsfbpf.a
