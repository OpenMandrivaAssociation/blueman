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

%{python_sitelib}/blueman
%{python_sitearch}/*.so
%{_libdir}/%{name}-*


%changelog
* Thu Jun 14 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.23-2
+ Revision: 805708
- rel bump
- files into both packages fix
- version update 1.23

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 1.21-2mdv2011.0
+ Revision: 595015
- rebuild for py 2.7

* Sat Dec 26 2009 Emmanuel Andry <eandry@mandriva.org> 1.21-1mdv2010.1
+ Revision: 482499
- New version 1.21
- update BR
- update files list

* Wed Jul 29 2009 Eugeni Dodonov <eugeni@mandriva.com> 1.10-3mdv2010.0
+ Revision: 403707
- Bring back .so files to prevent blueman-* from crashing on startup.

* Sat Jul 25 2009 Emmanuel Andry <eandry@mandriva.org> 1.10-1mdv2010.0
+ Revision: 399801
- New version 1.10
- add source url
- update files list

* Fri Mar 27 2009 Emmanuel Andry <eandry@mandriva.org> 1.02-4mdv2009.1
+ Revision: 361574
- don't explicitely requires notification-daemon

* Mon Mar 02 2009 Emmanuel Andry <eandry@mandriva.org> 1.02-3mdv2009.1
+ Revision: 347587
- requires python-blueman

* Mon Mar 02 2009 Emmanuel Andry <eandry@mandriva.org> 1.02-2mdv2009.1
+ Revision: 347346
- fix files
- BR python-dbus
- fix BR
- BR python-devel
- import blueman

