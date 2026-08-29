%define url_ver %(echo %{version} | cut -c 1-3)
%define _disable_rebuild_configure 1

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.7.0
Release:	1
Group:		Graphical desktop/Xfce
License:	BSD
URL:		https://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	make
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/libwavelan.so
%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS NEWS README*
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop
