Summary:	Client library for the Single Sign On daemon - Qt 4 bindings
Summary(pl.UTF-8):	Biblioteka kliencka demona Single Sign On - wiązania Qt 4
Name:		libsignon-qt4
Version:	8.58
Release:	3
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://gitlab.com/accounts-sso/signond/tags?sort=updated_desc
Source0:	https://gitlab.com/accounts-sso/signond/repository/archive.tar.bz2?ref=VERSION_%{version}&fake_out=/signond-%{version}.tar.bz2
# Source0-md5:	9f98e0758f72ca81abea9ce46088d42b
Patch0:		signon-cryptsetup.patch
URL:		https://gitlab.com/accounts-sso/signond
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtDBus-devel >= 4
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	cryptsetup-devel
BuildRequires:	doxygen
BuildRequires:	libproxy-devel
BuildRequires:	pkgconfig
Obsoletes:	libsignon-qt < 8.58-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Client library for the Single Sign On daemon - Qt 4 bindings.

%description -l pl.UTF-8
Biblioteka kliencka demona Single Sign On - wiązania Qt 4.

%package devel
Summary:	Header files for Single Sign On daemon Qt 4 client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki klienckiej Qt 4 demona Single Sign On
Group:		Development/Libraries
Requires:	QtCore-devel >= 4
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libsignon-qt-devel < 8.58-3

%description devel
Header files for Single Sign On daemon Qt 4 client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki klienckiej Qt 4 demona Single Sign On.

%package static
Summary:	Static libsignon-qt library
Summary(pl.UTF-8):	Statyczna biblioteka libsignon-qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsignon-qt library.

%description static -l pl.UTF-8
Statyczna biblioteka libsignon-qt.

%prep
%setup -q -n signond-VERSION_%{version}-aa1bcf3c9218addbdb376a40151b689409046125
%patch0 -p1

%build
#install -d build-qt5
#cd build-qt5
#qmake-qt5 ../signon.pro \
#	CONFIG+=cryptsetup \
#	BUILD_DIR="build-qt5" \
#	LIBDIR="%{_libdir}" \
#	QMAKE_CXX="%{__cxx}" \
#	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
#	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
#
#%{__make}
#cd ..

install -d build-qt4/lib/SignOn
cd build-qt4/lib/SignOn
qmake-qt4 ../../../lib/SignOn/SignOn.pro \
	CONFIG+=cryptsetup \
	BUILD_DIR="build-qt4" \
	LIBDIR="%{_libdir}" \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-qt4/lib/SignOn install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so.1.?

# packaged in signon.spec
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libsignon-qt/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libsignon-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignon-qt.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignon-qt.so
%{_includedir}/signon-qt
%{_pkgconfigdir}/libsignon-qt.pc
%{_libdir}/cmake/SignOnQt

%files static
%defattr(644,root,root,755)
%{_libdir}/libsignon-qt.a
