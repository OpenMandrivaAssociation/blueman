Name: 		blueman
Version: 	1.02
Release: 	%mkrel 1
Summary: 	Full featured bluetooth manager for GNOME/GTK
License: 	GPLv2+
Group: 		Communications
Url: 		http://blueman-project.org/
Source0: 	%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  glib2-devel
BuildRequires:  libGConf2-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  intltool
BuildRequires:	startup-notification-devel
BuildRequires:	python-gobject
BuildRequires:	python-notify
BuildRequires:	bluez-devel
BuildRequires:	python-devel
BuildRequires:	python-pyrex
BuildRequires:	python-dbus
Requires:	obex-data-server
Requires:	python-notify
Requires:	pygtk2.0
Requires:	gnome-python-gconf
Requires:	python-dbus
Requires:	python-gobject
Requires:	policykit-gnome
Requires:	notification-daemon
Buildroot: 	%_tmppath/%{name}-%{version}


%description
Blueman is designed to provide simple, yet effective means for 
controlling BlueZ API and simplifying bluetooth tasks such as:

* Connecting to 3G/EDGE/GPRS via dial-up
* Connecting to/Creating bluetooth networks
* Connecting to input devices
* Connecting to audio devices
* Sending/Receiving/Browsing files via OBEX
* Pairing

Blueman also integrates with Network Manager 0.7, so any Dialup/Network
 connections will be made available (via HAL) to Network Manager.

%package -n	python-%{name}
Summary:	Blueman python package
Group:		Communications

%description -n	python-%{name}
The python-blueman package is required for blueman.

%prep
%setup -q

%build
%configure2_5x --disable-desktop-update --disable-icon-update --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="HardwareSettings" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}-manager.desktop

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%post_install_gconf_schemas blueman-manager
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas blueman-manager

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%if %mdkversion < 200900
%update_menus
%endif

%if %mdkversion < 200900
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/dbus-1/system.d/org.%{name}*.conf
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}-*
%{_datadir}/applications/%{name}-manager.desktop
%{_datadir}/PolicyKit/policy/org.%{name}.policy
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/%{name}/icons/hicolor/*/*s/*.png
%{_datadir}/%{name}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/dbus-1/services/%{name}-applet.service
%{_datadir}/dbus-1/system-services/org.%{name}*.service
%{_datadir}/hal/fdi/information/20thirdparty/*.fdi
%{_mandir}/man1/%{name}*1.*

%files -n python-%{name}
%{py_puresitedir}/*
%{py_platsitedir}/*
%{_libdir}/%{name}-*


