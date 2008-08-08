%define pkgname kaa-metadata

Summary: Kaa Media Meta Data retrieval framework
Name: python-%{pkgname}
Version: 0.7.3
Release: %mkrel 2
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
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


