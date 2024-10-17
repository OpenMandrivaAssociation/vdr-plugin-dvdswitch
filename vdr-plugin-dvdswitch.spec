
%define plugin	dvdswitch

Summary:	VDR plugin: allows to play DVD-Images
Name:		vdr-plugin-%plugin
Version:	0.1.3
Release:	8
Group:		Video
License:	GPL
URL:		https://www.vdr-wiki.de/wiki/index.php/Dvdswitch-plugin
Source:		http://download.schmidtie.de/vdr-%plugin-%{version}.tar.bz2
Patch0:		90_dvdswitch-0.1.3-1.5.4.dpatch
Patch1:		03_no-files-crash.dpatch
Patch2:		dvdswitch-0.1.3-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
DVDswitch-plugin for VDR.

%prep
%setup -q -n %plugin-%{version}
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
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY




