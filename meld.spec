%define shortver 3.18

Summary:	A visual diff and merge tool targeted at developers
Name:		meld
Version:	%{shortver}.0
Release:	1
Source0:	https://download.gnome.org/sources/%{name}/%{shortver}/%{name}-%{version}.tar.xz
License:	GPLv2+
URL:		http://meldmerge.org/
Group:		File tools
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils

#Requires:	pygtk2.0
Requires:	python-dbus
Requires:	python-gtksourceview
Requires:	python-gobject
Requires:	python-cairo
Requires:	python-gi-cairo
Requires:	%{name}-schemas = %{version}-%{release}

Suggests:	patch

%description
Meld is a visual diff and merge tool targeted at developers. Meld helps you
compare files, directories, and version controlled projects. It provides
two- and three-way comparison of both files and directories, and supports
many version control systems including Git, Mercurial, Bazaar and Subversion.

Meld helps you review code changes, understand patches, and makes enormous
merge conflicts slightly less painful.

%files -f %{name}.lang
%{_bindir}/%{name}
%dir %{py3_puresitedir}/%{name}
%{py3_puresitedir}/%{name}/*
%{py3_puresitedir}/%{name}-%{version}-py3.?.egg-info
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}*
%{_iconsdir}/hicolor/*/actions/%{name}*
%{_iconsdir}/HighContrast/*/apps/%{name}*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*
%doc README NEWS COPYING

#---------------------------------------------------------------------------

%package schemas
Summary:	Gsettings schema files for %{name}
License:	LGPLv2+
Group:		File tools
BuildArch:	noarch

%description schemas
This package provides the gsettings schemas for %{name}.

%files schemas
%{_datadir}/glib-2.0/schemas/org.gnome.*.gschema.xml

#---------------------------------------------------------------------------

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py --no-compile-schemas --no-update-icon-cache install --root=%{buildroot}

# remove versioned doc directory
rm -fr %{buildroot}%{_docdir}/%{name}-%{version}/

# locales
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

