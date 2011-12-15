Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.2.1
Release:	4
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	9519921d31d8c43d054dbc11e1f0733b
Patch0:		browser-plugin-webkit.patch
Patch1:		extension-delete.patch
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel >= 0.8.999
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.7.5
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 3.1.90
BuildRequires:	folks-devel >= 0.6.1
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gjs-devel >= 1.29.18
BuildRequires:	glib2-devel >= 1:2.29.10
BuildRequires:	gnome-bluetooth-devel >= 3.1.0
BuildRequires:	gnome-desktop-devel >= 3.1.90
BuildRequires:	gnome-menus-devel >= 3.1.90
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gsettings-desktop-schemas-devel >= 3.1.90
BuildRequires:	gstreamer-devel >= 0.10.21
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.21
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40
BuildRequires:	json-glib-devel >= 0.13.90
BuildRequires:	libcanberra-devel
BuildRequires:	libcroco-devel >= 0.6.2
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	mutter-devel >= 3.2.1
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= 0.100
BuildRequires:	pulseaudio-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.15.5
BuildRequires:	telepathy-logger-devel >= 0.2.4
BuildRequires:	xorg-lib-libXfixes-devel
# for libmozjs.so
BuildRequires:	xulrunner-libs
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,preun):	GConf2
Requires:	caribou >= 0.3.5
Requires:	evolution-data-server >= 3.1.90
Requires:	gnome-bluetooth-libs >= 3.1.0
Requires:	gnome-menus >= 3.1.90
Requires:	gnome-settings-daemon >= 3.1.90
Requires:	gsettings-desktop-schemas >= 3.1.90
Requires:	mutter >= 3.2.1
Requires:	nautilus >= 3.2.0
Requires:	telepathy-logger >= 0.2.4
%requires_eq	xulrunner-libs
Suggests:	gnome-contacts >= 3.2.0
Suggests:	gnome-icon-theme-symbolic >= 3.0.0
Provides:	gdm-wm = 3.2.1-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell is the defining technology of the GNOME 3 desktop user
experience. It provides core interface functions like switching to
windows and launching applications. GNOME Shell takes advantage of the
capabilities of modern graphics hardware and introduces innovative
user interface concepts to provide a delightful and easy to use
experience.

%package -n browser-plugin-%{name}
Summary:	gnome-shell plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka gnome-shell do przeglądarek WWW
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	mozilla-firefox-plugin-gnome-shell = %{version}-%{release}
Provides:	mozilla-plugin-gnome-shell = %{version}-%{release}
Obsoletes:	mozilla-firefox-plugin-gnome-shell < %{version}-%{release}
Obsoletes:	mozilla-plugin-gnome-shell < %{version}-%{release}

%description -n browser-plugin-%{name}
gnome-shell plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka gnome-shell do przeglądarek WWW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
export LD_LIBRARY_PATH=%{_libdir}/xulrunner
%configure \
	--with-ca-certificates=/etc/certs/ca-certificates.crt \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions

%{__make} install \
	INSTALL="install -p" \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT \
	mozillalibdir=%{_browserpluginsdir}

# TODO use rpath at link time instead of this hack
mv $RPM_BUILD_ROOT%{_bindir}/gnome-shell{,.bin}
cat > $RPM_BUILD_ROOT%{_bindir}/gnome-shell <<'EOF'
#!/bin/sh
LD_LIBRARY_PATH=%{_libdir}/xulrunner
export LD_LIBRARY_PATH
exec %{_bindir}/gnome-shell.bin "$@"
EOF
chmod a+rx $RPM_BUILD_ROOT%{_bindir}/gnome-shell

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-shell/libgnome-shell.la \
	$RPM_BUILD_ROOT%{_browserpluginsdir}/*.la

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

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_bindir}/gnome-shell.bin
%attr(755,root,root) %{_bindir}/gnome-shell-extension-tool
%attr(755,root,root) %{_libexecdir}/gnome-shell-calendar-server
%attr(755,root,root) %{_libexecdir}/gnome-shell-hotplug-sniffer
%attr(755,root,root) %{_libexecdir}/gnome-shell-perf-helper
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%dir %{_libdir}/gnome-shell
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_mandir}/man1/gnome-shell.1*

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libgnome-shell-browser-plugin.so
