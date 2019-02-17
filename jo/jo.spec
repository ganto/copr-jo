Name:           jo
Version:        1.2
Release:        0.1%{?dist}
Summary:        JSON output from a shell

License:        GPLv2
URL:            https://github.com/jpmens/jo
Source0:        https://github.com/jpmens/jo/releases/download/v%{version}/jo-%{version}.tar.gz

BuildRequires:  autoconf
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
%{_mandir}/man1/*

%changelog
* Mon Apr 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.1-0.2
- Trigger rebuild for Fedora 28

* Fri Feb 09 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.1-0.1
- Initial package
