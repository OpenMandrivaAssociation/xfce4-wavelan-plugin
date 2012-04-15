%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.5.10
Release:	1
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-wavelan-0.5.6-gold.patch
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfce4ui-devel >= 4.9.0
Obsoletes:	xfce-wavelan-plugin

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -q
#patch1 -p0

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -exec rm -rf {} \;

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop
