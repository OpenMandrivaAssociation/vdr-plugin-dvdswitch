
%define plugin	dvdswitch
%define name	vdr-plugin-%plugin
%define version	0.1.3
%define rel	5

Summary:	VDR plugin: allows to play DVD-Images
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Dvdswitch-plugin
Source:		http://download.schmidtie.de/vdr-%plugin-%version.tar.bz2
Patch0:		90_dvdswitch-0.1.3-1.5.4.dpatch
Patch1:		03_no-files-crash.dpatch
Patch2:		dvdswitch-0.1.3-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
DVDswitch-plugin for VDR.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep
chmod 0644 README HISTORY

%vdr_plugin_params_begin %plugin
# write debug info to DEBUGLOGFILE
var=DEBUGLOGFILE
param=--debug=DEBUGLOGFILE
# scriptname with path for reading DVD as a ISO Image File
var=READ_SCRIPT
param=--readscript=READ_SCRIPT
# scriptname with path for writing selected DVD Image
var=WRITE_SCRIPT
param=--writescript=WRITE_SCRIPT
# path to DVD Images. This option can be set in setup-menu.
var=IMAGE_PATH
param=--imagedir=IMAGE_PATH
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3-5mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3-4mdv2009.1
+ Revision: 359309
- rebuild for new vdr

* Sun Sep 07 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-3mdv2009.0
+ Revision: 282087
- rebuild due to missing package on x86_64

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-2mdv2009.0
+ Revision: 197921
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3-1mdv2009.0
+ Revision: 197655
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of vdr 1.5.4 (P0 from e-tobi)
- fix a crash (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-12mdv2008.1
+ Revision: 145074
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-11mdv2008.1
+ Revision: 103086
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-10mdv2008.0
+ Revision: 49992
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-9mdv2008.0
+ Revision: 42078
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-8mdv2008.0
+ Revision: 22742
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-7mdv2007.0
+ Revision: 90913
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-6mdv2007.1
+ Revision: 73985
- rebuild for new vdr
- Import vdr-plugin-dvdswitch

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2007.0
- rebuild for new vdr

* Thu Jun 22 2006 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2007.0
- initial Mandriva release

