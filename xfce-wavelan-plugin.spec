%define oname xfce4-wavelan-plugin

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce-wavelan-plugin
Version:	0.5.4
Release:	%mkrel 2
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{oname}
Source0:	http://goodies.xfce.org/releases/%{oname}/%{oname}-%{version}.tar.bz2
BuildRequires:	xfce-panel-devel >= 4.4.1
BuildRequires:	perl(XML::Parser)
Requires:	xfce-panel >= 4.4.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{oname}

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/xfce4/panel-plugins/%{oname}
%{_datadir}/xfce4/panel-plugins/*.desktop
