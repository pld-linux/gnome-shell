Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.0.1
Release:	2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	d20a2d748bfed2f62e579962fdad0a06
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel >= 0.8.995
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel >= 0.7.11
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-bluetooth-devel >= 3.0.0
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gsettings-desktop-schemas-devel >= 3.0.0
BuildRequires:	gstreamer-devel >= 0.10.21
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.21
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.26
BuildRequires:	libcanberra-devel
BuildRequires:	libcroco-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	mutter-devel >= 3.0.1
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= 0.100
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel
BuildRequires:	telepathy-glib-devel >= 0.14.0
BuildRequires:	telepathy-logger-devel >= 0.2.4
BuildRequires:	xorg-lib-libXfixes-devel
# for libmozjs.so
BuildRequires:	xulrunner-libs
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,preun):	GConf2
Requires:	gnome-bluetooth-libs >= 3.0.0
Requires:	gnome-settings-daemon >= 3.0.0
Requires:	gsettings-desktop-schemas >= 0.1.7
Requires:	mutter >= 3.0.1
%requires_eq	xulrunner-libs
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
%{__aclocal} -I m4
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

mv $RPM_BUILD_ROOT%{_bindir}/gnome-shell{,.bin}
cat > $RPM_BUILD_ROOT%{_bindir}/gnome-shell <<'EOF'
#!/bin/sh
LD_LIBRARY_PATH=%{_libdir}/xulrunner
export LD_LIBRARY_PATH
exec %{_bindir}/gnome-shell.bin "${@}"
EOF
chmod a+rx $RPM_BUILD_ROOT%{_bindir}/gnome-shell

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-shell/libgnome-shell.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-shell.schemas
%glib_compile_schemas

%preun
%gconf_schema_uninstall gnome-shell.schemas

%postun
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_bindir}/gnome-shell.bin
%attr(755,root,root) %{_bindir}/gnome-shell-extension-tool
%attr(755,root,root) %{_libdir}/gnome-shell-calendar-server
%attr(755,root,root) %{_libdir}/gnome-shell-perf-helper
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%dir %{_libdir}/gnome-shell
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell.so
%{_libdir}/gnome-shell/Gdm-1.0.typelib
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_mandir}/man1/gnome-shell.1*
