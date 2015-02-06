%define pkgname kaa-metadata

Summary: Kaa Media Meta Data retrieval framework
Name: python-%{pkgname}
Version: 0.7.7
Release: 3
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

%dir %py_platsitedir/kaa/metadata/audio
%py_platsitedir/kaa/metadata/audio/*.py

%dir %py_platsitedir/kaa/metadata/audio/eyeD3
%py_platsitedir/kaa/metadata/audio/eyeD3/*.py

%dir %py_platsitedir/kaa/metadata/disc
%py_platsitedir/kaa/metadata/disc/*.py
%py_platsitedir/kaa/metadata/disc/*.so

%dir %py_platsitedir/kaa/metadata/games
%py_platsitedir/kaa/metadata/games/*.py

%dir %py_platsitedir/kaa/metadata/image
%py_platsitedir/kaa/metadata/image/*.py

%dir %py_platsitedir/kaa/metadata/misc
%py_platsitedir/kaa/metadata/misc/*.py

%dir %py_platsitedir/kaa/metadata/video
%py_platsitedir/kaa/metadata/video/*.py




%changelog
* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.7.7-1mdv2011.0
+ Revision: 591925
- New release

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.5-4mdv2010.0
+ Revision: 442213
- rebuild

  + Crispin Boylan <crisb@mandriva.org>
    - Use platform site dir
    - Use proper file list

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 0.7.5-2mdv2009.1
+ Revision: 320637
- rebuild for new python

* Sun Dec 21 2008 Crispin Boylan <crisb@mandriva.org> 0.7.5-1mdv2009.1
+ Revision: 316961
- New release

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 0.7.3-3mdv2009.0
+ Revision: 278260
- rebuild for new libdvdread

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.7.3-2mdv2009.0
+ Revision: 269028
- rebuild early 2009.0 package (before pixel changes)

* Mon May 12 2008 Crispin Boylan <crisb@mandriva.org> 0.7.3-1mdv2009.0
+ Revision: 206409
- New release

* Wed Feb 06 2008 Crispin Boylan <crisb@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 163252
- New release

* Fri Dec 28 2007 Crispin Boylan <crisb@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 138785
- New version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Crispin Boylan <crisb@mandriva.org> 0.6.1-1mdv2008.0
+ Revision: 17244
- New release


* Fri Mar 16 2007 Crispin Boylan <crisb@mandriva.org> 0.6.0-3mdv2007.1
+ Revision: 145306
- Provides python-mm to ease upgrading
- Requires python-kaa-base

* Wed Mar 14 2007 Crispin Boylan <crisb@mandriva.org> 0.6.0-2mdv2007.1
+ Revision: 143358
- Obsoletes python-mm

* Sun Mar 11 2007 Crispin Boylan <crisb@mandriva.org> 0.6.0-1mdv2007.1
+ Revision: 141409
- Initial Mandriva package
- Create python-kaa-metadata

