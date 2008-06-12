%define name powerprefs 
%define version 0.5.0
%define release %mkrel 1

Name: %{name}
Summary: Configuration Client for pbbuttonsd 
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/pbbuttons/%{name}-%{version}.tar.bz2
Source1:        %name-16x16.png.bz2
Source2:        %name-32x32.png.bz2
Source3:        %name-48x48.png.bz2
URL: http://pbbuttons.sourceforge.net/projects/powerprefs/index.html
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: pbbuttonsd >= 0.5
BuildRequires: pbbuttonsd-devel >= 0.5
BuildRequires: libgtk+2-devel
ExclusiveArch: ppc

%description
A frontend for pbbuttonsd to allow the configuration of powersaving 
and keyboard settings on many Apple PowerBooks and iBooks (TM). 

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
%makeinstall_std
(cd %{buildroot}
mkdir -p .%{_libdir}/menu
cat > .%{_libdir}/menu/powerprefs <<EOF
?package(powerprefs):\
command="%{_bindir}/powerprefs"\
title="Powerprefs"\
longtitle="Config Client for pbbuttonsd"\
needs="x11"\
section="System/Configuration/Hardware"\
icon="%{name}.png"
EOF
)

#icon
# icon
install -d $RPM_BUILD_ROOT/%{_miconsdir}
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING README TODO
%{_bindir}/powerprefs
%{_mandir}/man*/*
%{_libdir}/menu/*
%{_datadir}/powerprefs/pixmaps/*.xpm
%_miconsdir/*
%_iconsdir/*
%_liconsdir/*

