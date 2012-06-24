Summary:	GPhotoFS - FUSE module that exposes cameras as filesystems
Summary(pl):	GPhotoFS - modu� FUSE pokazuj�cy aparaty jako systemu plik�w
Name:		gphotofs
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	73b7582888b19d2ed976849a6a02782a
URL:		http://gphoto.sourceforge.net/proj/gphotofs/
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	libfuse-devel >= 0:2.2
BuildRequires:	libgphoto2-devel >= 2.1
BuildRequires:	pkgconfig
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

%description -l pl
GPhotoFS to klient systemu plik�w oparty na libgphoto2 pokazuj�cy
obs�ugiwane aparaty jako systemy plik�w; o ile niekt�re aparaty
implementuj� klas� USB Mass Storage i s� dost�pne jako systemy plik�w
(co czyni ten program nadmiarowym), to wiele u�ywa PTP (Picture
Transfer Protocol - protoko�u przesy�ania zdj��) lub innego w�asnego
protoko�u. O ile aparat jest obs�ugiwany przez libgphoto2, mo�e by�
podmontowany jako system plik�w przy u�yciu tego programu.

Jako �e libgphoto2 jest bibliotek� przestrzeni u�ytkownika do
komunikacji z aparatami, naturalnym jest, �e aby stworzy� na jej
podstawie system plik�w, nale�y u�y� FUSE - i w�a�nie to zosta�o
zrobione.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gphotofs
