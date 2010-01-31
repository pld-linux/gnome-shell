Summary:	Window and compositing manager based on Clutter
Name:		gnome-shell
Version:	2.28.0
Release:	4
License:	GPL v2+
Group:		X11/Window Managers
URL:		http://git.gnome.org/cgit/gnome-shell
Source0:	http://download.gnome.org/sources/gnome-shell/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	a9f93a6f03da60f2f6e3fb82a9e7dc94
BuildRequires:	clutter-devel
BuildRequires:	gettext-devel
BuildRequires:	gir-repository-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool >= 0.26
BuildRequires:	librsvg-devel
BuildRequires:	mutter-devel
BuildRequires:	pango-devel >= 1:1.26.0
BuildRequires:	pkgconfig >= 0.16
BuildRequires:	rpm-pythonprov
# for libmozjs.so
BuildRequires:	xulrunner-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A window manager based on metacity and clutter

%package devel
Summary:	Development package for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc
Requires:	pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q

%build
export LD_LIBRARY_PATH=%{_libdir}/xulrunner
%configure \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-shell.schemas
/sbin/ldconfig

%preun
%gconf_schema_uninstall gnome-shell.schemas

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-shell
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/mutter/plugins/*.so
%attr(755,root,root) %{_libdir}/mutter/plugins/*.la
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
