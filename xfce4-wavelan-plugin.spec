%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.5.6
Release:	%mkrel 2
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-wavelan-0.5.6-gold.patch
BuildRequires:	xfce4-panel-devel >= 4.7
BuildRequires:	perl(XML::Parser)
BuildRequires:	libxfce4util-devel
BuildRequires:	libxfcegui4-devel
Requires:	xfce4-panel >= 4.7
Obsoletes:	xfce-wavelan-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -q
%patch1 -p0
autoconf

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel-plugins/%{name}
%{_datadir}/xfce4/panel-plugins/*.desktop
