Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.8.0.1
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	f6511b663a9e3eda6f640bfab7a8fa08
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	NetworkManager-devel >= 0.9.6
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	caribou-devel >= 0.4.8
BuildRequires:	clutter-devel >= 1.13.4
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 3.5.3
BuildRequires:	gcr-devel >= 3.3.90
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gjs-devel >= 1.35.4
BuildRequires:	glib2-devel >= 1:2.35.0
BuildRequires:	gnome-bluetooth-devel >= 3.1.0
BuildRequires:	gnome-desktop-devel >= 3.7.90
BuildRequires:	gnome-menus-devel >= 3.5.3
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gsettings-desktop-schemas-devel >= 3.7.4
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.7.9
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.40
BuildRequires:	json-glib-devel >= 0.13.90
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libcroco-devel >= 0.6.8
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	mutter-devel >= 3.8.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= 0.100
BuildRequires:	pulseaudio-devel >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= 0.11
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= 0.17.5
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.35.0
Requires:	at-spi2-atk >= 2.4.0
Requires:	caribou >= 0.4.8
Requires:	evolution-data-server >= 3.5.3
Requires:	gjs >= 1.35.4
Requires:	glib2 >= 1:2.35.0
Requires:	gnome-bluetooth-libs >= 3.1.0
Requires:	gnome-menus >= 3.5.3
Requires:	gnome-settings-daemon >= 3.1.90
Requires:	gsettings-desktop-schemas >= 3.7.4
Requires:	gtk+3 >= 3.7.9
Requires:	mutter >= 3.8.0
Requires:	nautilus >= 3.2.0
Requires:	telepathy-mission-control
Suggests:	gnome-contacts >= 3.2.0
Suggests:	gnome-icon-theme-symbolic >= 3.0.0
Provides:	gdm-wm = 3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell is the defining technology of the GNOME 3 desktop user
experience. It provides core interface functions like switching to
windows and launching applications. GNOME Shell takes advantage of the
capabilities of modern graphics hardware and introduces innovative
user interface concepts to provide a delightful and easy to use
experience.

%package apidocs
Summary:	GNOME Shell API documentation
Summary(pl.UTF-8):	Dokumentacja API GNOME Shell
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
This package provides GNOME Shell API documentation.

%description apidocs -l pl.UTF-8
Ten pakiet dostarcza dokumentację API GNOME Shell.

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

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-shell/{extensions,search-providers}

%{__make} install \
	INSTALL="install -p" \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT \
	mozillalibdir=%{_browserpluginsdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-shell/*.la \
	$RPM_BUILD_ROOT%{_browserpluginsdir}/*.la
# evolution already ships this file
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/evolution-calendar.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

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
%attr(755,root,root) %{_bindir}/gnome-shell-extension-prefs
%attr(755,root,root) %{_bindir}/gnome-shell-extension-tool
%attr(755,root,root) %{_bindir}/gnome-shell-perf-tool
%attr(755,root,root) %{_libexecdir}/gnome-shell-calendar-server
%attr(755,root,root) %{_libexecdir}/gnome-shell-hotplug-sniffer
%attr(755,root,root) %{_libexecdir}/gnome-shell-perf-helper
%dir %{_libdir}/gnome-shell
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell.so
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell-js.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/ShellJS-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-shell
%{_desktopdir}/gnome-shell.desktop
%{_desktopdir}/gnome-shell-extension-prefs.desktop
%{_mandir}/man1/gnome-shell.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/shell
%{_gtkdocdir}/st

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_browserpluginsdir}/libgnome-shell-browser-plugin.so
