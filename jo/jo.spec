Name:           jo
Version:        1.1
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

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc
%{_bindir}/*
%{_mandir}/man1/*

%changelog
