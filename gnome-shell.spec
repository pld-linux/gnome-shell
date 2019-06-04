%define		caribou_version 0.4.8
%define		clutter_version 1.21.5
%define		evolution_data_server_version 3.18.0
%define		gcr_version 3.7.5
%define		gjs_version 1.47.0
%define		glib2_version 1:2.46.0
%define		gnome_bluetooth_version 3.9.0
%define		gnome_desktop_version 3.7.90
%define		gnome_menus_version 3.5.3
%define		gsettings_desktop_schemas_version 3.22.0
%define		gtk_version 3.15.0
%define		json_glib_version 0.13.90
%define		libcroco_version 0.6.8
%define		mutter_version 3.30.0
%define		networkmanager_version 0.9.8
%define		polkit_version 0.100
%define		pulseaudio_version 2.0
%define		startup_notification_version 0.11
%define		telepathy_glib_version 0.17.5

Summary:	Window manager and application launcher for GNOME
Name:		gnome-shell
Version:	3.32.2
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	632b67075ebdc183f94461fa05a8505b
URL:		http://live.gnome.org/GnomeShell
BuildRequires:	NetworkManager-devel >= %{networkmanager_version}
BuildRequires:	NetworkManager-gtk-lib-devel >= %{networkmanager_version}
BuildRequires:	clutter-devel >= %{clutter_version}
BuildRequires:	evolution-data-server-devel >= %{evolution_data_server_version}
BuildRequires:	gcr-devel >= %{gcr_version}
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	gjs-devel >= %{gjs_version}
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gnome-bluetooth-devel >= %{gnome_bluetooth_version}
BuildRequires:	gnome-common
BuildRequires:	gnome-control-center-devel
BuildRequires:	gnome-desktop-devel >= %{gnome_desktop_version}
BuildRequires:	gnome-menus-devel >= %{gnome_menus_version}
BuildRequires:	gobject-introspection-devel >= 1.50.0
BuildRequires:	gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_version}
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= %{gtk_version}
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	ibus-devel
BuildRequires:	json-glib-devel >= %{json_glib_version}
BuildRequires:	libcanberra-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libcroco-devel >= 0.6.8
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.42.0
BuildRequires:	mutter-devel >= %{mutter_version}
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= %{polkit_version}
BuildRequires:	pulseaudio-devel >= %{pulseaudio_version}
BuildRequires:	python3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	ruby-sass
BuildRequires:	sassc
BuildRequires:	startup-notification-devel >= %{startup_notification_version}
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-glib-devel >= %{telepathy_glib_version}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	NetworkManager-libs >= %{networkmanager_version}
Requires:	at-spi2-atk >= 2.4.0
Requires:	caribou-libs >= %{caribou_version}
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
Requires:	telepathy-logger-libs >= 0.2
Requires:	telepathy-mission-control
Suggests:	gnome-contacts >= 3.2.0
Suggests:	gnome-icon-theme-symbolic >= 3.8.0
Provides:	gdm-wm = 3.8.0
Obsoletes:	browser-plugin-gnome-shell < 3.32.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Shell is the defining technology of the GNOME 3 desktop user
experience. It provides core interface functions like switching to
windows and launching applications. GNOME Shell takes advantage of the
capabilities of modern graphics hardware and introduces innovative
user interface concepts to provide a delightful and easy to use
experience.

%package devel
Summary:	Development files for GNOME Shell
Summary(pl.UTF-8):	Pliki programistyczne dla GNOME Shell
Group:		Development/Libraries

%description devel
This package provides development files for GNOME Shell.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla GNOME Shell.

%package apidocs
Summary:	GNOME Shell API documentation
Summary(pl.UTF-8):	Dokumentacja API GNOME Shell
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
This package provides GNOME Shell API documentation.

%description apidocs -l pl.UTF-8
Ten pakiet dostarcza dokumentację API GNOME Shell.

%prep
%setup -q

%build
%meson build \
	-Dgtk_doc=true
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome-shell/{extensions,search-providers}

%meson_install -C build

# evolution already ships this file
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/evolution-calendar.desktop

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-shell/libgnome-shell*.a

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%attr(755,root,root) %{_bindir}/gnome-shell-extension-prefs
%attr(755,root,root) %{_bindir}/gnome-shell-extension-tool
%attr(755,root,root) %{_bindir}/gnome-shell-perf-tool
%attr(755,root,root) %{_libexecdir}/gnome-shell-calendar-server
%attr(755,root,root) %{_libexecdir}/gnome-shell-hotplug-sniffer
%attr(755,root,root) %{_libexecdir}/gnome-shell-overrides-migration.sh
%attr(755,root,root) %{_libexecdir}/gnome-shell-perf-helper
%attr(755,root,root) %{_libexecdir}/gnome-shell-portal-helper
%dir %{_libdir}/gnome-shell
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell.so
%attr(755,root,root) %{_libdir}/gnome-shell/libgnome-shell-menu.so
%attr(755,root,root) %{_libdir}/gnome-shell/libgvc.so
%attr(755,root,root) %{_libdir}/gnome-shell/libst-1.0.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-shell
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_desktopdir}/gnome-shell-extension-prefs.desktop
%{_desktopdir}/org.gnome.Shell.desktop
%{_desktopdir}/org.gnome.Shell.PortalHelper.desktop
%{_mandir}/man1/gnome-shell.1*
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%{systemduserunitdir}/gnome-shell-wayland.target
%{systemduserunitdir}/gnome-shell-x11.target
%{systemduserunitdir}/gnome-shell.service

%files devel
%defattr(644,root,root,755)
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/shell
%{_gtkdocdir}/st
