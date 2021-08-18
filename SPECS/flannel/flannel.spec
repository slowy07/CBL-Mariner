%global debug_package %{nil}
%define our_gopath %{_topdir}/.gopath

Summary:        Simple and easy way to configure a layer 3 network fabric designed for Kubernetes
Name:           flannel
Version:        0.14.0
Release:        1%{?dist}
License:        Apache License 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Libraries
URL:            https://github.com/coreos/flannel
#Source0:       https://github.com/coreos/flannel/archive/v0.14.0.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  golang >= 1.10.3
BuildRequires:  kernel-headers

%description
Flannel is a simple and easy way to configure a layer 3 network fabric designed for Kubernetes.

%prep
%autosetup -p1

%build
export GOPATH=%{our_gopath}
export TAG=v%{version}
%ifarch x86_64
export ARCH=amd64
%endif
%ifarch aarch64
export ARCH=arm64
%endif
export CGO_ENABLED=1

make dist/flanneld

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ./dist/flanneld

%clean
rm -rf %{buildroot}/*

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/flanneld

%changelog
* Fri Aug 06 2021 Nicolas Guibourge <nicolasg@microsoft.com> 0.14.0-1
- Move to version 0.14.0 and build using golang 1.16.7.
* Tue Jun 08 2021 Henry Beberman <henry.beberman@microsoft.com> 0.12.0-3
- Increment release to force republishing using golang 1.15.13.
* Mon Apr 26 2021 Nicolas Guibourge <nicolasg@microsoft.com> 0.12.0-2
- Increment release to force republishing using golang 1.15.11.
* Wed Jan 20 2021 Nicolas Guibourge <nicolasg@microsoft.com> - 0.12.0-1
- Original version for CBL-Mariner.
