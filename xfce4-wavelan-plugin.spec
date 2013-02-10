%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	WaveLAN plugin for the Xfce panel
Name:		xfce4-wavelan-plugin
Version:	0.5.11
Release:	2
Group:		Graphical desktop/Xfce
License:	BSD
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-wavelan-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
Patch1:		xfce4-wavelan-0.5.6-gold.patch
BuildRequires:	xfce4-panel-devel >= 4.9.0
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.9.0

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

chmod +x %{buildroot}%{_libdir}/xfce4/panel/plugins/libwavelan.so
%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
* Sun Apr 15 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.10-1
+ Revision: 791184
- fix file list
- update to new version 0.5.10
- spec file clean

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.5.6-2
+ Revision: 790094
- Rebuild for xfce 4.10

* Sun Dec 12 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.6-1mdv2011.0
+ Revision: 620598
- update to new version 0.5.6
- update buildrequires
- update URL for Source0

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-2mdv2010.1
+ Revision: 543442
- rebuild for mdv 2010.1

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.5-1mdv2010.0
+ Revision: 373806
- update to new version 0.5.5

* Fri Mar 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-8mdv2009.1
+ Revision: 349483
- rebuild for xfce-4.6.0

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-7mdv2009.1
+ Revision: 295032
- rebuild for new Xfce4.6 beta1

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.5.4-6mdv2009.0
+ Revision: 262414
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.5.4-5mdv2009.0
+ Revision: 256998
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-3mdv2008.1
+ Revision: 110559
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING file
- use upstream name
- fix path

* Sun Jun 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.4-1mdv2008.0
+ Revision: 34783
- Import xfce-wavelan-plugin

