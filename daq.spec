
Summary:	Data Acquisition Library
Name:		daq
Version:	0.6.2
Release:	1
License:	GNU General Public License
Group:		Networking
Source0:	http://www.snort.org/dl/snort-current/%{name}-%{version}.tar.gz
# Source0-md5:	6ea8aaa6f067f8b8ef6de45b95d55875
URL:		http://www.snort.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libdnet-devel
BuildRequires:	libnetfilter_queue-devel
BuildRequires:	libpcap-devel >= 1.0.0
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
%attr(755,root,root) %{_libdir}/lib*.so*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/daq-modules-config
