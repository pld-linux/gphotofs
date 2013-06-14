Summary:	GPhotoFS - FUSE module that exposes cameras as filesystems
Summary(pl.UTF-8):	GPhotoFS - moduł FUSE pokazujący aparaty jako systemy plików
Name:		gphotofs
Version:	0.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	bf88054e726e27b9c699ac4ed594cdf6
Patch0:		%{name}-po.patch
URL:		http://gphoto.sourceforge.net/proj/gphotofs/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	libfuse-devel >= 0:2.6
BuildRequires:	libgphoto2-devel >= 2.5
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.6
Requires:	libfuse >= 0:2.6
Requires:	libgphoto2 >= 2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPhotoFS is a filesystem client based on libgphoto2 that exposes
supported cameras as filesystems; while some cameras implement the USB
Mass Storage class and already appear as filesystems (making this
program redundant), many use the Picture Transfer Protocol (PTP) or
some other custom protocol. But as long as the camera is supported
by libgphoto2, it can be mounted as a filesystem using this program.

As libgphoto2 is a userspace library for interacting with cameras, it
is natural that if one to build a filesystem ontop of it, one should
use FUSE, and that is what have been done.

%description -l pl.UTF-8
GPhotoFS to klient systemu plików oparty na libgphoto2 pokazujący
obsługiwane aparaty jako systemy plików; o ile niektóre aparaty
implementują klasę USB Mass Storage i są dostępne jako systemy plików
(co czyni ten program nadmiarowym), to wiele używa PTP (Picture
Transfer Protocol - protokołu przesyłania zdjęć) lub innego własnego
protokołu. O ile aparat jest obsługiwany przez libgphoto2, może być
podmontowany jako system plików przy użyciu tego programu.

Jako że libgphoto2 jest biblioteką przestrzeni użytkownika do
komunikacji z aparatami, naturalnym jest, że aby stworzyć na jej
podstawie system plików, należy użyć FUSE - i właśnie to zostało
zrobione.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal} -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gphotofs
