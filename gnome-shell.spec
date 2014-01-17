# TODO: wayland support
#
%define		caribou_version 0.4.8
%define		clutter_version 1.13.4
%define		evolution_data_server_version 3.5.3
%define		gcr_version 3.7.5
%define		gjs_version 1.38.1
%define		glib2_version 1:2.37.0
%define		gnome_bluetooth_version 3.9.0
%define		gnome_desktop_version 3.7.90
%define		gnome_menus_version 3.5.3
%define		gsettings_desktop_schemas_version 3.7.4
%define		gtk_version 3.7.9
%define		json_glib_version 0.13.90
%define		libcroco_version 0.6.8
%define		mutter_version 3.10.1
%define		networkmanager_version 0.9.8
%define		polkit_version 0.100
%define		pulseaudio_version 2.0
%define		startup_notification_version 0.11
%define		telepathy_glib_version 0.17.5

Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.10.3
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	82c51189b192241391c6c632d5a1a92a
Patch0:		link.patch
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	NetworkManager-devel >= %{networkmanager_version}
BuildRequires:	NetworkManager-gtk-lib-devel >= %{networkmanager_version}
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	caribou-devel >= %{caribou_version}
BuildRequires:	clutter-devel >= %{clutter_version}
BuildRequires:	evolution-data-server-devel >= %{evolution_data_server_version}
BuildRequires:	gcr-devel >= %{gcr_version}
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	gjs-devel >= %{gjs_version}
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gnome-bluetooth-devel >= %{gnome_bluetooth_version}
BuildRequires:	gnome-control-center-devel
BuildRequires:	gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires:	gnome-menus-devel >= %{gnome_menus_version}
BuildRequires:	gobject-introspection-devel >= 0.10.1
BuildRequires:	gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.7.9
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.40
BuildRequires:	json-glib-devel >= %{json_glib_version}
BuildRequires:	libcanberra-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libcroco-devel >= 0.6.8
BuildRequires:	libsecret-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	mutter-devel >= %{mutter_version}
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= %{polkit_version}
BuildRequires:	pulseaudio-devel >= %{pulseaudio_version}
BuildRequires:	python >= 2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	startup-notification-devel >= %{startup_notification_version}
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= %{telepathy_glib_version}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	NetworkManager-libs >= %{networkmanager_version}
Requires:	at-spi2-atk >= 2.4.0
Requires:	caribou >= %{caribou_version}
Requires:	clutter >= %{clutter_version}
Requires:	evolution-data-server >= %{evolution_data_server_version}
Requires:	gcr >= %{gcr_version}
Requires:	gjs >= %{gjs_version}
Requires:	glib2 >= %{glib2_version}
Requires:	gnome-bluetooth-libs >= %{gnome_bluetooth_version}
Requires:	gnome-desktop >= %{gnome_desktop_version}
Requires:	gnome-menus >= %{gnome_menus_version}
Requires:	gnome-settings-daemon >= 3.8.0
Requires:	gnome-themes-standard
Requires:	gsettings-desktop-schemas >= %{gsettings_desktop_schemas_version}
Requires:	gtk+3 >= %{gtk_version}
Requires:	json-glib >= %{json_glib_version}
Requires:	libcroco >= %{libcroco_version}
Requires:	mutter >= %{mutter_version}
Requires:	nautilus >= 3.8.0
Requires:	polkit >= %{polkit_version}
Requires:	pulseaudio-libs >= %{pulseaudio_version}
Requires:	startup-notification >= %{startup_notification_version}
Requires:	telepathy-glib >= %{telepathy_glib_version}
Requires:	telepathy-mission-control
Suggests:	gnome-contacts >= 3.2.0
Suggests:	gnome-icon-theme-symbolic >= 3.8.0
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

%description -n browser-plugin-%{name}
gnome-shell plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka gnome-shell do przeglądarek WWW.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell-menu.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/ShellJS-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_libdir}/gnome-shell/ShellMenu-0.1.typelib
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
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
