%define pkgname kaa-metadata

Summary: Kaa Media Meta Data retrieval framework
Name: python-%{pkgname}
Version: 0.7.5
Release: %mkrel 3
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
%py_puresitedir/kaa_metadata*.egg-info

%dir %py_puresitedir/kaa/metadata
%py_puresitedir/kaa/metadata/*.py
%py_puresitedir/kaa/metadata/*.pyc
%py_puresitedir/kaa/metadata/*.pyo

%dir %py_puresitedir/kaa/metadata/audio
%py_puresitedir/kaa/metadata/audio/*.py
%py_puresitedir/kaa/metadata/audio/*.pyc
%py_puresitedir/kaa/metadata/audio/*.pyo

%dir %py_puresitedir/kaa/metadata/audio/eyeD3
%py_puresitedir/kaa/metadata/audio/eyeD3/*.py
%py_puresitedir/kaa/metadata/audio/eyeD3/*.pyc
%py_puresitedir/kaa/metadata/audio/eyeD3/*.pyo

%dir %py_puresitedir/kaa/metadata/disc
%py_puresitedir/kaa/metadata/disc/*.py
%py_puresitedir/kaa/metadata/disc/*.pyc
%py_puresitedir/kaa/metadata/disc/*.pyo
%py_puresitedir/kaa/metadata/disc/*.so

%dir %py_puresitedir/kaa/metadata/games
%py_puresitedir/kaa/metadata/games/*.py
%py_puresitedir/kaa/metadata/games/*.pyc
%py_puresitedir/kaa/metadata/games/*.pyo

%dir %py_puresitedir/kaa/metadata/image
%py_puresitedir/kaa/metadata/image/*.py
%py_puresitedir/kaa/metadata/image/*.pyc
%py_puresitedir/kaa/metadata/image/*.pyo

%dir %py_puresitedir/kaa/metadata/misc
%py_puresitedir/kaa/metadata/misc/*.py
%py_puresitedir/kaa/metadata/misc/*.pyc
%py_puresitedir/kaa/metadata/misc/*.pyo

%dir %py_puresitedir/kaa/metadata/video
%py_puresitedir/kaa/metadata/video/*.py
%py_puresitedir/kaa/metadata/video/*.pyc
%py_puresitedir/kaa/metadata/video/*.pyo


