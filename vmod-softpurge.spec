Summary: Soft purge support for Varnish VCL
Name: vmod-softpurge
Version: 0.2
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-softpurge.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish > 4.0
BuildRequires: make, python-docutils

%description
Soft purge support for Varnish VCL

%prep
%setup -n libvmod-softpurge

%build
# this assumes that VARNISHSRC is defined on the rpmbuild command line, like this:
# rpmbuild -bb --define 'VARNISHSRC /home/user/rpmbuild/BUILD/varnish-3.0.3' redhat/*spec
./configure VARNISHSRC=%{VARNISHSRC} VMODDIR="$(PKG_CONFIG_PATH=%{VARNISHSRC} pkg-config --variable=vmoddir varnishapi)" --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
make
make check

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/doc/%{name}
cp LICENSE COPYING README.rst %{buildroot}/usr/share/doc/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.
