%define ver    3.16
%define micro  1

Summary:    GNOME 3 visual diff and merge tool
Name:       meld
Version:    %{ver}.%{micro}
Release:    1
Source0:    https://download.gnome.org/sources/%{name}/%{ver}/%{name}-%{version}.tar.xz
License:    GPLv2+
URL:        http://meldmerge.org/
Group:      File tools
BuildArch:  noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  desktop-file-utils

Requires:  pygtk2.0
Requires:  python2
Requires:  python2-gtksourceview
Requires:  python2-gobject

%description
Meld is a GNOME 2 visual diff and merge tool. It integrates especially well
with CVS. The diff viewer lets you edit files in place (diffs update
dynamically), and a middle column shows detailed changes and allows merges.
The margins show location of changes for easy navigation, and it also
features a tabbed interface that allows you to open many diffs at once.

%files -f FILELIST -f %name.lang
%doc README
%doc NEWS
%doc COPYING

%prep
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py --no-compile-schemas --no-update-icon-cache install --root=%{buildroot} --record=FILELIST

# remove duplicates (by rpm5 point of view) from FILELIST
# (see http://wiki.rosalab.ru/ru/index.php/Python_policy#Automated_setup)
%__sed -i -e /pyc$/d FILELIST

# manpage uses xz compression
%__sed -i -e 's|%{name}.1|%{name}.1.xz|' FILELIST

# .desktop
desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*

# locales
%find_lang %{name} --with-gnome

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
