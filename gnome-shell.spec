#
# Conditional build:
%bcond_without	apidocs	# API documentation

%define		clutter_ver			1.21.5
# max(ecal_req, eds_req)
%define		evolution_data_server_ver	3.33.1
%define		gcr_ver				3.7.5
%define		gjs_ver				1.65.1
%define		glib_ver			1:2.57.2
%define		gnome_bluetooth_ver		3.9.0
%define		gnome_desktop_ver		3.36.0
%define		gsettings_desktop_schemas_ver	3.33.1
%define		gtk_ver				3.15.0
%define		json_glib_ver			0.13.90
%define		libcroco_ver			0.6.8
%define		libsecret_ver			0.18
%define		mutter_ver			3.38.0
%define		NetworkManager_ver		1.10.4
%define		polkit_ver			0.100
%define		pulseaudio_ver			13
%define		startup_notification_ver	0.11

Summary:	Window manager and application launcher for GNOME
Summary(pl.UTF-8):	Zarządca okien i uruchamiania aplikacji dla GNOME
Name:		gnome-shell
Version:	3.38.4
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	https://download.gnome.org/sources/gnome-shell/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	e6c891c430016ced449e38661ddf6dec
URL:		https://wiki.gnome.org/Projects/GnomeShell
BuildRequires:	NetworkManager-devel >= %{NetworkManager_ver}
BuildRequires:	at-spi2-atk-devel
BuildRequires:	bash-completion-devel >= 2.0
BuildRequires:	clutter-devel >= %{clutter_ver}
BuildRequires:	evolution-data-server-devel >= %{evolution_data_server_ver}
BuildRequires:	gcr-devel >= %{gcr_ver}
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	gjs-devel >= %{gjs_ver}
BuildRequires:	glib2-devel >= %{glib_ver}
BuildRequires:	gnome-autoar-devel
BuildRequires:	gnome-bluetooth-devel >= %{gnome_bluetooth_ver}
BuildRequires:	gnome-control-center-devel
# for cldr2json.py (through pygobject->gi)
BuildRequires:	gnome-desktop >= %{gnome_desktop_ver}
BuildRequires:	gobject-introspection-devel >= 1.50.0
BuildRequires:	gsettings-desktop-schemas-devel >= %{gsettings_desktop_schemas_ver}
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= %{gtk_ver}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.15}
BuildRequires:	ibus-devel >= 1.5.2
BuildRequires:	json-glib-devel >= %{json_glib_ver}
BuildRequires:	libcanberra-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libcroco-devel >= %{libcroco_ver}
BuildRequires:	libsecret-devel >= %{libsecret_ver}
BuildRequires:	libsoup-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.53.0
BuildRequires:	mutter-devel >= %{mutter_ver}
BuildRequires:	ninja >= 1.5
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	polkit-devel >= %{polkit_ver}
BuildRequires:	pulseaudio-devel >= %{pulseaudio_ver}
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-pygobject3 >= 3
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	sassc
BuildRequires:	sed >= 4.0
BuildRequires:	startup-notification-devel >= %{startup_notification_ver}
BuildRequires:	systemd-devel
BuildRequires:	systemd-units
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= %{glib_ver}
# gjs->gi->NMA.gir
Requires:	NetworkManager-libs >= %{NetworkManager_ver}
Requires:	adwaita-icon-theme
Requires:	at-spi2-atk >= 2.4.0
Requires:	clutter >= %{clutter_ver}
Requires:	evolution-data-server >= %{evolution_data_server_ver}
Requires:	gcr >= %{gcr_ver}
Requires:	gjs >= %{gjs_ver}
Requires:	glib2 >= %{glib_ver}
Requires:	gnome-bluetooth-libs >= %{gnome_bluetooth_ver}
Requires:	gnome-desktop >= %{gnome_desktop_ver}
Requires:	gnome-settings-daemon >= 3.8.0
Requires:	gsettings-desktop-schemas >= %{gsettings_desktop_schemas_ver}
Requires:	gtk+3 >= %{gtk_ver}
Requires:	ibus >= 1.5.2
Requires:	json-glib >= %{json_glib_ver}
Requires:	libcroco >= %{libcroco_ver}
Requires:	libsecret >= %{libsecret_ver}
Requires:	mutter >= %{mutter_ver}
Requires:	nautilus >= 3.8.0
Requires:	polkit >= %{polkit_ver}
Requires:	pulseaudio-libs >= %{pulseaudio_ver}
Requires:	startup-notification >= %{startup_notification_ver}
# gjs->gir->TelepathyGLib
Requires:	telepathy-glib >= 0.17.5
# gjs->gir->TelepathyLogger
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

%description -l pl.UTF-8
GNOME Shell to technologia definiująca doznania użytkownika środowiska
graficznego GNOME 3. Zapewnia podstawowe funkcje interfejsu, takie jak
przełączanie między oknami czy uruchamianie aplikacji. GNOME Shell
wykorzystuje mozliwości współczesnego sprzętu graficznego i wprowadza
innowacyjne koncepcje interfejsu użytkownika, zapewniające przyjemne
doznania i łatwość użycia.

%package -n bash-completion-gnome-shell
Summary:	Bash completion for GNOME Shell commands
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów poleceń GNOME Shell
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-gnome-shell
Bash completion for GNOME Shell commands.

%description -n bash-completion-gnome-shell -l pl.UTF-8
Bashowe dopełnianie parametrów poleceń GNOME Shell.

%package devel
Summary:	Development files for GNOME Shell
Summary(pl.UTF-8):	Pliki programistyczne dla GNOME Shell
Group:		Development/Libraries
BuildArch:	noarch

%description devel
This package provides development files for GNOME Shell.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki programistyczne dla GNOME Shell.

%package apidocs
Summary:	GNOME Shell API documentation
Summary(pl.UTF-8):	Dokumentacja API GNOME Shell
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
This package provides GNOME Shell API documentation.

%description apidocs -l pl.UTF-8
Ten pakiet dostarcza dokumentację API GNOME Shell.

%prep
%setup -q

%{__sed} -i -e '/^libshew =/ s/ library/ shared_library/' subprojects/shew/src/meson.build

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true}

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
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-extensions
%attr(755,root,root) %{_bindir}/gnome-extensions-app
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
%attr(755,root,root) %{_libdir}/gnome-shell/libshew-0.so
%attr(755,root,root) %{_libdir}/gnome-shell/libst-1.0.so
%{_libdir}/gnome-shell/Gvc-1.0.typelib
%{_libdir}/gnome-shell/Shell-0.1.typelib
%{_libdir}/gnome-shell/St-1.0.typelib
%dir %{_libdir}/gnome-shell/girepository-1.0
%{_libdir}/gnome-shell/girepository-1.0/Shew-0.typelib
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
%{_datadir}/dbus-1/services/org.gnome.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Notifications.service
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Screencast.service
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_datadir}/gnome-shell
%{_datadir}/metainfo/org.gnome.Extensions.metainfo.xml
%{_datadir}/xdg-desktop-portal/portals/gnome-shell.portal
%{_desktopdir}/org.gnome.Extensions.desktop
%{_desktopdir}/org.gnome.Shell.desktop
%{_desktopdir}/org.gnome.Shell.Extensions.desktop
%{_desktopdir}/org.gnome.Shell.PortalHelper.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Extensions.Devel.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Extensions.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg
%{_mandir}/man1/gnome-extensions.1*
%{_mandir}/man1/gnome-shell.1*
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%{systemduserunitdir}/org.gnome.Shell.target
%{systemduserunitdir}/org.gnome.Shell-disable-extensions.service
%{systemduserunitdir}/org.gnome.Shell@wayland.service
%{systemduserunitdir}/org.gnome.Shell@x11.service

%files -n bash-completion-gnome-shell
%defattr(644,root,root,755)
%{bash_compdir}/gnome-extensions

%files devel
%defattr(644,root,root,755)
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/shell
%{_gtkdocdir}/st
%endif
