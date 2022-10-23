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

Requires:	obex-data-server
Requires:	python-notify
Requires:	pygtk2.0
Requires:	gnome-python2-gconf
Requires:	python2-dbus
Requires:	python2-gobject3
Requires:	polkit-gnome
Requires:	python2-blueman
Requires:	python2

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
%{_bindir}/%{name}-*
%{_libexecdir}/blueman-mechanism
%{_datadir}/applications/%{name}-manager.desktop
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_datadir}/%{name}/ui/*.ui
#{_datadir}/%{name}/icons/hicolor/*/*s/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
#{_datadir}/blueman/icons/hicolor/scalable/actions/*.svg
#{_datadir}/blueman/icons/hicolor/scalable/devices/*.svg
#{_datadir}/blueman/icons/hicolor/scalable/status/*.svg
#{_datadir}/dbus-1/services/%{name}-applet.service
%{_datadir}/dbus-1/system-services/org.%{name}*.service
%{_mandir}/man1/%{name}*1.* 
 
#---------------------------------------------------------

%package -n	python2-%{name}
Summary:	Blueman python package
Group:		Communications

%description -n	python2-%{name}
The python-blueman package is required for blueman.

%files -n python2-%{name}
#{py2_puresitedir}/blueman
#{py2_platsitedir}/*.so


#-----------------------------------------------------------

%package -n	nautilus-sendto-%{name} 
Summary:	Blueman nautilus plugin
Group:		Communications
Provides:	nautilus-sendto-%{name}-plugin

%description -n	nautilus-sendto-%{name}
Blueman nautilus plugin



%files -n nautilus-sendto-%{name}
#{_libdir}/nautilus-sendto/plugins/libnstblueman.so

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
