Name:           unicode-ucd
Version:        15.1.0
Release:        1
Summary:        Unicode Character Database
License:        Unicode-DFS-2016 AND Unicode-TOU
URL:            http://www.unicode.org/ucd/
Source0:        http://www.unicode.org/Public/zipped/%{version}/UCD.zip
Source1:        http://www.unicode.org/Public/zipped/%{version}/Unihan.zip
Source2:        https://www.unicode.org/license.txt
BuildArch:      noarch

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%package unihan
Summary:        Unicode Han Database
Requires:       %{name} = %{version}-%{release}

%description unihan
This package contains Unihan.zip which contains the data files for the Unified
Han database of Hanzi/Kanji/Hanja Chinese characters.

%prep
%autosetup -p1 -c
grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)

%build

%install
mkdir -p %{buildroot}%{_datadir}/unicode/ucd
cp -ar . %{buildroot}%{_datadir}/unicode/ucd
cp %{S:1} %{buildroot}%{_datadir}/unicode/ucd/

%files
%dir %{_datadir}/unicode
%{_datadir}/unicode/ucd
%exclude %{_datadir}/unicode/ucd/Unihan.zip

%files unihan
%{_datadir}/unicode/ucd/Unihan.zip
