#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

%define _sbindir /sbin

Name:           parted
Version:        3.0
Release:        1
License:        GPL-3.0+
Summary:        The GNU disk partition manipulation program
Url:            http://www.gnu.org/software/parted
Group:          Applications/System

Source0:        ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  pkgconfig(ext2fs)

%description
The GNU Parted program allows you to create, destroy, resize, move,
and copy hard disk partitions. Parted can be used for creating space
for new operating systems, reorganizing disk usage, and copying data
to new hard disks.

%package devel
Summary:        Files for developing apps which will manipulate disk partitions
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
The GNU Parted library is a set of routines for hard disk partition
manipulation. If you want to develop programs that manipulate disk
partitions and filesystems using the routines provided by the GNU
Parted library, you need to install this package.

%prep
%setup -q

%build
%configure --disable-static --disable-device-mapper --with-readline --with-libdir=%{_libdir} --exec-prefix=/usr
make %{?_smp_mflags}

%install
%make_install

# Remove components we do not ship
rm -rf %{buildroot}%{_infodir}/dir

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%lang_package

%docs_package

%files
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/parted
%{_sbindir}/partprobe
%{_libdir}/libparted*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/parted
%{_libdir}/libparted.so
%{_libdir}/pkgconfig/libparted.pc

