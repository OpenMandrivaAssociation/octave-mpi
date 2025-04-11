%global octpkg mpi

Summary:	Octave bindings for basic Message Passing Interface (MPI) functions for paralle
Name:		octave-mpi
Version:	3.1.0
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/mpi/
Url:		https://github.com/carlodefalco/octave-mpi/
Source0:	https://github.com/carlodefalco/octave-mpi/releases/download/v%{version}/mpi-%{version}.tar.gz
# https://github.com/carlodefalco/octave-mpi/issues/5
# https://github.com/carlodefalco/octave-mpi/issues/6
Patch0:		octave-mpi-3.1.0-octave8.patch

BuildRequires:  octave-devel >= 4.4.0
BuildRequires:	pkgconfig(ompi)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Octave bindings for basic Message Passing Interface (MPI) functions
for parallel computing.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
export CPPFLAGS="%{optflags} -I /usr/include/openmpi-%{?_arch}/"
export MPICC="%{_libdir}/openmpi/bin/mpic++"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

