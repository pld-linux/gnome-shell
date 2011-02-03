Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	2.91.6
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	fe4fffc4725c4cdb85c3500117eef936
Patch0:		gtk3.patch
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.5.12
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel >= 0.7.8
BuildRequires:	glib2-devel >= 1:2.26.0
#BuildRequires:	gnome-bluetooth >= 2.90
BuildRequires:	gnome-desktop3-devel >= 2.91.4
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	gstreamer-devel >= 0.10.16
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.16
BuildRequires:	gtk+3-devel >= 2.91.7
BuildRequires:	intltool >= 0.26
BuildRequires:	libcanberra-devel
BuildRequires:	libcroco-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	mutter-devel >= 2.91.4
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libXfixes-devel
# for libmozjs.so
BuildRequires:	xulrunner-libs
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,preun):	GConf2
Requires:	gnome-settings-daemon >= 2.91.8
Requires:	gsettings-desktop-schemas
Requires:	mutter >= 2.91.4
Suggests:	gtk3-engines-themes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell is the defining technology of the GNOME 3 desktop user
experience. It provides core interface functions like switching to
windows and launching applications. GNOME Shell takes advantage of the
capabilities of modern graphics hardware and introduces innovative
user interface concepts to provide a delightful and easy to use
experience.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export LD_LIBRARY_PATH=%{_libdir}/xulrunner
%configure \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/mutter/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-shell.schemas
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas

%preun
%gconf_schema_uninstall gnome-shell.schemas

%postun
if [ "$1" = "0" ]; then
	%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_libdir}/mutter/plugins/libgnome-shell.so
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%{_sysconfdir}/xdg/menus/gs-applications.menu
%{_libdir}/gnome-shell
%{_datadir}/glib-2.0/schemas/org.gnome.accessibility.magnifier.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_mandir}/man1/gnome-shell.1*
