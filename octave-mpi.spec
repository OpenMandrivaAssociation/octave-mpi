%define octpkg mpi

Summary:	Octave bindings for basic MPI functions for parallel computing
Name:		octave-%{octpkg}
Version:	3.1.0
Release:	1
Url:		https://github.com/carlodefalco/octave-%{octpkg}/
Source0:	%{url}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
#Patch0:		%{name}-1.2.0-octave-4.1-compatibility.patch
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 3.6.4
BuildRequires:	pkgconfig(ompi)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Octave bindings for basic Message Passing Interface (MPI) functions for
parallel computing.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n octave-%{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
export MPICC="%{_libdir}/openmpi/bin/mpic++"
%set_build_flags
%octave_pkg_build

%install
#export MPICC="%{_libdir}/openmpi/bin/mpic++"
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

