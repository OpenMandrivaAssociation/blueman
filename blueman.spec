Name: 		blueman
Version: 	1.23
Release: 	3
Summary: 	Full featured bluetooth manager for GNOME/GTK
License: 	GPLv2+
Group: 		Communications
Url: 		http://blueman-project.org/
Source0: 	http://launchpad.net/blueman/1.0/1.10/+download/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pygtk2.0-devel
BuildRequires:  intltool
BuildRequires:	startup-notification-devel
BuildRequires:	python2-gobject
BuildRequires:	python2-notify
BuildRequires:	bluez-devel
BuildRequires:	python2-devel
BuildRequires:	python2-pyrex
BuildRequires:	python2-dbus
Requires:	obex-data-server
Requires:	python2-notify
Requires:	pygtk2.0
Requires:	gnome-python2-gconf
Requires:	python2-dbus
Requires:	python2-gobject
Requires:	polkit-gnome
Requires:	python-blueman


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

%package -n	nautilus-sendto-%{name} 
Summary:	Blueman nautilus plugin
Group:		Communications
Provides:	nautilus-sendto-%{name}-plugin

%description -n	nautilus-sendto-%{name}
Blueman nautilus plugin


%prep
%setup -q

%build
ln -s %{_bindir}/python2 python
export PATH=`pwd`:$PATH

%configure2_5x  --disable-desktop-update \
		--disable-icon-update \
	    --disable-schemas-install \
		--disable-static
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="HardwareSettings" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}-manager.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/dbus-1/system.d/org.%{name}*.conf
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}-*
%{_datadir}/applications/%{name}-manager.desktop
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/%{name}/icons/hicolor/*/*s/*.png
#%{_datadir}/%{name}/icons/hicolor/scalable/status/*.svg
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/blueman/icons/hicolor/scalable/actions/*.svg
%{_datadir}/blueman/icons/hicolor/scalable/devices/*.svg
%{_datadir}/blueman/icons/hicolor/scalable/status/*.svg
%{_datadir}/dbus-1/services/%{name}-applet.service
%{_datadir}/dbus-1/system-services/org.%{name}*.service
#%{_datadir}/hal/fdi/information/20thirdparty/*.fdi
%{_mandir}/man1/%{name}*1.*

%files -n nautilus-sendto-%{name}
%{_libdir}/nautilus-sendto/plugins/libnstblueman.so

%files -n python-%{name}

%{python2_sitelib}/blueman
%{python2_sitearch}/*.so
%{_libdir}/%{name}-*


