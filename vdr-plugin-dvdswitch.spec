
%define plugin	dvdswitch
%define name	vdr-plugin-%plugin
%define version	0.1.2
%define rel	10

Summary:	VDR plugin: allows to play DVD-Images
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.vdr-wiki.de/wiki/index.php/Dvdswitch-plugin
Source:		http://download.schmidtie.de/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
DVDswitch-plugin for VDR.

%prep
%setup -q -n %plugin-%version
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


