Summary:	GObject-based wrapper around the Exiv2 library
Name:		libgexiv2
Version:	0.10.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://download.gnome.org/sources/gexiv2/0.10/gexiv2-%{version}.tar.xz
# Source0-md5:	ba3e5f4e9e4b68822c80276014b5d61b
BuildRequires:	exiv2-devel
BuildRequires:	glib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gexiv2 is a GObject-based wrapper around the Exiv2 library.
It makes the basic features of Exiv2 available to GNOME applications.

%package devel
Summary:	Header files for gexiv2 library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	zlib-devel

%description devel
This is the package containing the header files for gexiv2 library.

%prep
%setup -qn gexiv2-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgexiv2.so.?
%attr(755,root,root) %{_libdir}/libgexiv2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgexiv2.so
%{_includedir}/gexiv2
%{_pkgconfigdir}/gexiv2.pc
%{_datadir}/vala/vapi/gexiv2.vapi

