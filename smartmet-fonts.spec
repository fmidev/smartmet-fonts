%define BINNAME fonts
Summary: fonts
Name: smartmet-%{BINNAME}
Version: 22.8.19
Release: 1.fmi
License: MIT
BuildArch: noarch
Group: Development/Tools
URL: https://github.com/fmidev/smartmet-fonts
Source0: %{name}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Provides: smartmet-fonts
Conflicts: fmifonts <= 20.12.9

%description
Weather fonst used by SmartMet software

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{BINNAME}
 
%build

%install
mkdir -m 0755 -p $RPM_BUILD_ROOT/%{_datadir}/fonts/smartmet
install -m 644 otf/*.otf $RPM_BUILD_ROOT/%{_datadir}/fonts/smartmet/
install -m 644 ttf/Mirri.ttf $RPM_BUILD_ROOT/%{_datadir}/fonts/smartmet/
install -m 644 Fontmap.GS $RPM_BUILD_ROOT/%{_datadir}/fonts/smartmet/

%clean
rm -rf $RPM_BUILD_ROOT

%post
fc-cache

%postun
fc-cache

%files
%defattr(-,root,root,0775)
%{_datadir}/fonts/smartmet/

%changelog
* Fri Aug 19 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.19-1.fmi
- Initial version extracted from the private fmifonts package
