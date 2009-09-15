%define pkgname kaa-metadata

Summary: Kaa Media Meta Data retrieval framework
Name: python-%{pkgname}
Version: 0.7.5
Release: %mkrel 4
Source0: http://mesh.dl.sourceforge.net/sourceforge/freevo/%{pkgname}-%{version}.tar.gz
License: LGPL
URL: http://sourceforge.net/projects/freevo/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: python-devel
BuildRequires: libdvdread-devel
BuildRequires: python-kaa-base
Requires:	python-kaa-base
Provides:	python-mm
Obsoletes:	python-mm

%description
kaa-metadata is a Media Meta Data retrieval framework. 
It retrieves metadata from mp3, ogg, avi, jpg, tiff and 
other file formats. Among others it thereby parses ID3v2, 
ID3v1, EXIF, IPTC and Vorbis data into an object oriented 
struture.  It is the successor to mmpython.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)

%_bindir/mminfo
%py_platsitedir/kaa_metadata*.egg-info

%dir %py_platsitedir/kaa/metadata
%py_platsitedir/kaa/metadata/*.py
%py_platsitedir/kaa/metadata/*.pyc
%py_platsitedir/kaa/metadata/*.pyo

%dir %py_platsitedir/kaa/metadata/audio
%py_platsitedir/kaa/metadata/audio/*.py
%py_platsitedir/kaa/metadata/audio/*.pyc
%py_platsitedir/kaa/metadata/audio/*.pyo

%dir %py_platsitedir/kaa/metadata/audio/eyeD3
%py_platsitedir/kaa/metadata/audio/eyeD3/*.py
%py_platsitedir/kaa/metadata/audio/eyeD3/*.pyc
%py_platsitedir/kaa/metadata/audio/eyeD3/*.pyo

%dir %py_platsitedir/kaa/metadata/disc
%py_platsitedir/kaa/metadata/disc/*.py
%py_platsitedir/kaa/metadata/disc/*.pyc
%py_platsitedir/kaa/metadata/disc/*.pyo
%py_platsitedir/kaa/metadata/disc/*.so

%dir %py_platsitedir/kaa/metadata/games
%py_platsitedir/kaa/metadata/games/*.py
%py_platsitedir/kaa/metadata/games/*.pyc
%py_platsitedir/kaa/metadata/games/*.pyo

%dir %py_platsitedir/kaa/metadata/image
%py_platsitedir/kaa/metadata/image/*.py
%py_platsitedir/kaa/metadata/image/*.pyc
%py_platsitedir/kaa/metadata/image/*.pyo

%dir %py_platsitedir/kaa/metadata/misc
%py_platsitedir/kaa/metadata/misc/*.py
%py_platsitedir/kaa/metadata/misc/*.pyc
%py_platsitedir/kaa/metadata/misc/*.pyo

%dir %py_platsitedir/kaa/metadata/video
%py_platsitedir/kaa/metadata/video/*.py
%py_platsitedir/kaa/metadata/video/*.pyc
%py_platsitedir/kaa/metadata/video/*.pyo


