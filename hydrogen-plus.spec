Summary:        An unofficial extension to Hydrogen
Name:           hydrogen-plus
Version:        1
Release:        1%{dist}
License:        GPLv3
URL:            https://nothingneko.com
Source0:        https://github.com/nothingneko/hydrogen-plus/archive/refs/heads/main.zip
BuildArch:      noarch

%description
An unofficial extension to Hydrogen.

%install
# Install licenses
mkdir -p licenses
install -pm 0644 LICENSE licenses/LICENSE

%files
%license licenses/LICENSE
%doc README.md
%{_datadir}/Hydrogen-Plus/*

%changelog
* Wed Jan 9 2023 Jaiden Riordan <jade@fyralabs.com> - 1.1-1
- Init
