
Summary:	Data Acquisition Library
Name:		daq
Version:	0.6.1
Release:	1
License:	GNU General Public License
Group:		Networking
Source0:	daq-%{version}.tar.gz
# Source0-md5:	54ed07a9e903512260fbc30f902748fd
URL:		http://www.snort.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libpcap-devel >= 1.0.0
BuildRequires:	libdnet-devel
BuildRequires:	libnetfilter_queue-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data Acquisition library for Snort.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

%configure \
	--enable-ipv6

%{__make}

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
%{_includedir}/*.h
%{_libdir}/daq
%{_libdir}/daq/daq_*.so
%{_libdir}/lib*.so*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/daq-modules-config
