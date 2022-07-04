Name:           jo
Version:        1.4
Release:        0.2%{?dist}
Summary:        JSON output from a shell

License:        GPLv2
URL:            https://github.com/jpmens/jo
Source0:        https://github.com/jpmens/jo/releases/download/%{version}/jo-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  pandoc

%description
jo is a small utility to create JSON objects

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%check
make check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/*
%{_sysconfdir}/bash_completion.d/jo.bash
%{_mandir}/man1/*

%changelog
* Thu Jul 23 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.4-0.1
- Update to 1.4

* Sun Feb 02 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.3-0.1
- Update to 1.3

* Sun Feb 17 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.2-0.2
- Add gcc to BuildRequires to fix build failure on >= Fedora 29

* Sun Feb 17 2019 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.2-0.1
- Update to 1.2

* Mon Apr 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.1-0.2
- Trigger rebuild for Fedora 28

* Fri Feb 09 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.1-0.1
- Initial package

