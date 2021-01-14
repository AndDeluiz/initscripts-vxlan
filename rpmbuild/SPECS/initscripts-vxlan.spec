Name:		initscripts-vxlan
Version:	0.2
Release:	2%{?dist}
Summary:	vxlan ifup/down scripts
Packager:       Anderson Deluiz
Group:		System Environment/Base
License:	GPLv2 and GPLv2+
URL:		https://github.com/anddeluiz/initscripts-vxlan

Source:		%{name}-%{version}.tar.gz

Requires:	initscripts >= 9.49.30
Requires:	iproute >= 3.10


%description
initscripts-vxlan provides scripts to manage vxlan netwok intefaces on the host machine

%prep
%setup -q


%install
%{__mkdir} -p %{buildroot}/etc/sysconfig/network-scripts

%{__install} -p -m 0755 ifup-vxlan   %{buildroot}/etc/sysconfig/network-scripts/
%{__install} -p -m 0755 ifdown-vxlan %{buildroot}/etc/sysconfig/network-scripts/

%files
%defattr(-,root,root)
/etc/sysconfig/network-scripts/ifup-vxlan
/etc/sysconfig/network-scripts/ifdown-vxlan

%doc


%changelog


