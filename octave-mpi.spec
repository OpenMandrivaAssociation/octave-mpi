%define octpkg mpi

# Exclude .oct files from provides
%define __provides_exclude_from ^%{octpkglibdir}/.*.oct$

Summary:	Octave bindings for basic MPI functions for parallel computing
Name:		octave-%{octpkg}
Version:	1.2.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:		%{name}-1.2.0-octave-4.1-compatibility.patch
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.6.4
BuildRequires:	mpi-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Octave bindings for basic Message Passing Interface (MPI) functions for
parallel computing.

This package is part of community Octave-Forge collection.

%prep
%setup -q -c %{octpkg}-%{version}
cp %SOURCE0 .

# Apply patch
pushd %{octpkg}
%patch0 -p1
popd

%build
export MPICC="%{_libdir}/openmpi/bin/mpic++"
%octave_pkg_build #-T

%install
export MPICC="%{_libdir}/openmpi/bin/mpic++"
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/README
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

