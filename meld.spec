Summary:    A visual diff and merge tool targeted at developers
Name:       meld
Version:    3.16.1
Release:    2
Source0:    https://download.gnome.org/sources/%{name}/3.16/%{name}-%{version}.tar.xz
License:    GPLv2+
URL:        http://meldmerge.org/
Group:      File tools
BuildArch:  noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxml2-utils
BuildRequires:  desktop-file-utils

Requires:  pygtk2.0
Requires:  python2-gtksourceview
Requires:  python2-gobject

%description
Meld is a visual diff and merge tool targeted at developers. Meld helps you
compare files, directories, and version controlled projects. It provides
two- and three-way comparison of both files and directories, and supports
many version control systems including Git, Mercurial, Bazaar and Subversion.

Meld helps you review code changes, understand patches, and makes enormous
merge conflicts slightly less painful.

%files -f %name.lang -f FILELIST
%doc README NEWS COPYING

%prep
%setup -q

%build
%{__python2} setup.py build

%install
%{__python2} setup.py --no-compile-schemas --no-update-icon-cache install --root=%{buildroot} --record=FILELIST

# remove duplicates (by rpm5 point of view) from FILELIST
# (see http://wiki.rosalab.ru/ru/index.php/Python_policy#Automated_setup)
sed -i -e /pyc$/d FILELIST

# manpage uses xz compression
sed -i -e 's|%{name}.1|%{name}.1.xz|' FILELIST

# .desktop
desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*

# locales
%find_lang %{name} --with-gnome

