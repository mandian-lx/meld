%define name	meld
%define version 1.3.1
%define release %mkrel 1

Summary:	GNOME 2 visual diff and merge tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: meld-1.2-make-install.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
License:	GPLv2+
URL:		http://meld.sourceforge.net/
Group:		File tools
BuildRequires: scrollkeeper
BuildRequires: python-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires:	pygtk2.0-libglade
Requires:	gnome-python
Requires:	gnome-python-canvas
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	patch
BuildArch:	noarch
Requires(post): scrollkeeper >= 0.3
Requires(postun): scrollkeeper >= 0.3


%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges.
The margins show location of changes for easy navigation, and it also
features a tabbed interface that allows you to open many diffs at once.

%prep
%setup -q
%patch -p1

%build
%make prefix=%_prefix libdir=%_datadir

%install
rm -rf ${RPM_BUILD_ROOT} %name.lang
%makeinstall_std prefix=%_prefix libdir=%_datadir

%find_lang %name --with-gnome

# Icons
install -D -m 644 glade2/pixmaps/16x16/meld.png ${RPM_BUILD_ROOT}%{_miconsdir}/%{name}.png
install -D -m 644 glade2/pixmaps/32x32/meld.png ${RPM_BUILD_ROOT}%{_iconsdir}/%{name}.png
install -D -m 644 glade2/pixmaps/48x48/meld.png ${RPM_BUILD_ROOT}%{_liconsdir}/%{name}.png

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


rm -rf %buildroot/usr/var/lib/scrollkeeper

%clean
rm -rf ${RPM_BUILD_ROOT}

%if %mdkversion < 200900
%post
%{update_menus}
%update_scrollkeeper
%postun
%{clean_menus}
%clean_scrollkeeper
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS MAINTAINERS NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%dir %{_datadir}/omf/%name
%{_datadir}/omf/%name/meld-*.omf
%{_datadir}/pixmaps/*
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

