Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.5.5
Release:	%mkrel 1
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-wavelan-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -q

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
