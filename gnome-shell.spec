Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	2.31.4
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/2.31/%{name}-%{version}.tar.bz2
# Source0-md5:	ba8b85b3b723b6c1f05847cbe2fc06de
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	dbus-glib-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel >= 0.7
BuildRequires:	glib2-devel >= 1:2.25.9
BuildRequires:	gnome-desktop-devel >= 2.26.0
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	gstreamer-devel >= 0.10.16
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.16
BuildRequires:	gtk+2-devel >= 2:2.19.0
BuildRequires:	intltool >= 0.26
BuildRequires:	libcroco-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	mutter-devel >= 2.31.4
BuildRequires:	pango-devel >= 1:1.26.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpm-pythonprov
BuildRequires:	startup-notification-devel
# for libmozjs.so
BuildRequires:	xulrunner-libs
Requires(post,preun):	GConf2
Requires:	mutter >= 2.29.1
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

%preun
%gconf_schema_uninstall gnome-shell.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_bindir}/gnome-shell-clock-preferences
%attr(755,root,root) %{_libdir}/mutter/plugins/libgnome-shell.so
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%{_sysconfdir}/xdg/menus/gs-applications.menu
%{_libdir}/gnome-shell
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_desktopdir}/gnome-shell-clock-preferences.desktop
%{_mandir}/man1/gnome-shell.1*
