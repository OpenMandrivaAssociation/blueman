%define Werror_cflags %nil
%define _libexecdir /usr/libexec
%define _disable_ld_no_undefined 1

Name: 		blueman
Version: 	2.3.4
Release: 	1
Summary: 	Full featured bluetooth manager for GNOME/GTK
License: 	GPLv2+
Group: 		Communications
Url: 		https://github.com/blueman-project/blueman/
Source0:	https://github.com/blueman-project/blueman/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: perl(XML::Parser)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0) >= 0.9
BuildRequires: pkgconfig(bluez)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(dbus-python)
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: python-gobject3
BuildRequires: python3dist(cython)
BuildRequires: automake
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: iproute2
BuildRequires: meson

Requires:	polkit-gnome
Requires:	python-blueman
Requires:	python

Requires:	bluez
Requires:	python-gobject3
#Requires:	pulseaudio-module-bluetooth
Requires:	adwaita-icon-theme
Requires:	iproute2


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
 
%files -f %{name}.lang
#{_sysconfdir}/dbus-1/system.d/org.%{name}*.conf
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_prefix}/lib/systemd/system/blueman-mechanism.service
%{_prefix}/lib/systemd/user/blueman-applet.service
%{_bindir}/%{name}-*
%{_libexecdir}/blueman-mechanism
%{_libexecdir}/blueman-rfcomm-watcher
%{_datadir}/applications/%{name}-manager.desktop
%{_datadir}/applications/blueman-adapters.desktop
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/icons/hicolor/*x*/status/blueman*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/16x16/devices/blueman-device.png
%{_datadir}/icons/hicolor/scalable/actions/blueman*
%{_datadir}/icons/hicolor/scalable/devices/blueman*
%{_datadir}/icons/hicolor/scalable/emblems/
%{_datadir}/icons/hicolor/scalable/status/blueman*
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/blueman/pixmaps/
%{_datadir}/dbus-1/services/org.blueman.Applet.service
%{_datadir}/dbus-1/system.d/org.blueman.Mechanism.conf
%{_datadir}/glib-2.0/schemas/org.blueman.gschema.xml
%{_datadir}/dbus-1/system-services/org.%{name}*.service
%{_datadir}/nautilus-python/extensions/nautilus_blueman_sendto.py
%{_datadir}/nemo-python/extensions/nemo_blueman_sendto.py
%{_datadir}/Thunar/sendto/thunar-sendto-blueman.desktop
%{_datadir}/caja-python/extensions/caja_blueman_sendto.py
%{_mandir}/man1/%{name}*1.* 
 
#---------------------------------------------------------

%package -n	python-%{name}
Summary:	Blueman python package
Group:		Communications

%description -n	python-%{name}
The python-blueman package is required for blueman.

%files -n python-%{name}
%{python_sitelib}/_blueman.so
%{python_sitelib}/blueman/


#-----------------------------------------------------------


%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%meson \
       -Dpolicykit=true

%meson_build
%install
%meson_install


%find_lang %{name}
