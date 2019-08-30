%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.6.1
Release:	1
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -q

%build
%configure \
	--disable-static
%make_build

%install
%make_install

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/libwavelan.so
%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop
